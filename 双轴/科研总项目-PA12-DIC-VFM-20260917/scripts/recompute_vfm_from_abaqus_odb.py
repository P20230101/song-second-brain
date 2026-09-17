"""Recompute the elastic VFM equations from an Abaqus ODB.

The ODB supplies the independent FE stress/strain state and nodal reactions.
Virtual displacements are assigned at element nodes and interpolated with the
same bilinear CPS4R shape functions used by the reduced-integration model.
"""
from __future__ import print_function

import argparse
import itertools
import json
import math
import os

import numpy as np
import odbAccess


def component(field, value, label):
    return float(value.data[field.componentLabels.index(label)])


def virtual_fields(x, y, half_span):
    X = x / half_span
    Y = y / half_span
    inv = 1.0 / half_span
    return (
        (X, 0.0, inv, 0.0, 0.0),
        (0.0, Y, 0.0, inv, 0.0),
        (X * Y, 0.0, Y * inv, 0.0, X * inv),
        (0.0, X * Y, 0.0, X * inv, Y * inv),
        (X * Y * Y, 0.0, Y * Y * inv, 0.0, 2.0 * X * Y * inv),
        (0.0, Y * X * X, 0.0, X * X * inv, 2.0 * X * Y * inv),
        (X * X * X, Y, 3.0 * X * X * inv, inv, 0.0),
        (X, Y * Y * Y, inv, 3.0 * Y * Y * inv, 0.0),
    )


def shape(xi, eta):
    n = (
        0.25 * (1.0 - xi) * (1.0 - eta),
        0.25 * (1.0 + xi) * (1.0 - eta),
        0.25 * (1.0 + xi) * (1.0 + eta),
        0.25 * (1.0 - xi) * (1.0 + eta),
    )
    dxi = (
        -0.25 * (1.0 - eta),
        0.25 * (1.0 - eta),
        0.25 * (1.0 + eta),
        -0.25 * (1.0 + eta),
    )
    deta = (
        -0.25 * (1.0 - xi),
        -0.25 * (1.0 + xi),
        0.25 * (1.0 + xi),
        0.25 * (1.0 - xi),
    )
    return n, dxi, deta


def element_virtual_strains(coords, half_span):
    xi = 0.0
    eta = 0.0
    n, dxi, deta = shape(xi, eta)
    dx_dxi = sum(dxi[i] * coords[i][0] for i in range(4))
    dx_deta = sum(deta[i] * coords[i][0] for i in range(4))
    dy_dxi = sum(dxi[i] * coords[i][1] for i in range(4))
    dy_deta = sum(deta[i] * coords[i][1] for i in range(4))
    det_j = dx_dxi * dy_deta - dx_deta * dy_dxi
    if det_j <= 0.0:
        raise ValueError("Non-positive element Jacobian")
    integrated = np.zeros((8, 3), dtype=float)
    nodal_fields = [virtual_fields(point[0], point[1], half_span) for point in coords]
    for index in range(8):
        ux = [nodal_fields[i][index][0] for i in range(4)]
        uy = [nodal_fields[i][index][1] for i in range(4)]
        du_dxi = sum(dxi[i] * ux[i] for i in range(4))
        du_deta = sum(deta[i] * ux[i] for i in range(4))
        dv_dxi = sum(dxi[i] * uy[i] for i in range(4))
        dv_deta = sum(deta[i] * uy[i] for i in range(4))
        du_dx = (du_dxi * dy_deta - du_deta * dy_dxi) / det_j
        du_dy = (-du_dxi * dx_deta + du_deta * dx_dxi) / det_j
        dv_dx = (dv_dxi * dy_deta - dv_deta * dy_dxi) / det_j
        dv_dy = (-dv_dxi * dx_deta + dv_deta * dx_dxi) / det_j
        integrated[index, :] = det_j * 4.0 * np.asarray((du_dx, dv_dy, du_dy + dv_dx))
    return integrated


def fit(A, b, q_true):
    rank = int(np.linalg.matrix_rank(A))
    q = np.linalg.lstsq(A, b, rcond=None)[0] if rank == 4 else np.full(4, np.nan)
    error = float(np.max(np.abs((q - q_true) / q_true))) if rank == 4 else float("nan")
    residual = float(np.linalg.norm(A.dot(q) - b) / max(np.linalg.norm(b), np.finfo(float).eps)) if rank == 4 else float("nan")
    return {"rank": rank, "condition_number": float(np.linalg.cond(A)) if rank == 4 else float("inf"), "q_fit_MPa": q.tolist(), "max_relative_parameter_error": error, "relative_residual": residual}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("odb_path")
    parser.add_argument("output_json")
    parser.add_argument("--span-mm", type=float, default=100.0)
    parser.add_argument("--center-width-mm", type=float, default=20.0)
    parser.add_argument("--arm-thickness-mm", type=float, default=2.0)
    parser.add_argument("--center-thickness-mm", type=float, default=1.4)
    parser.add_argument("--q-true", nargs=4, type=float, default=(341.88034188034186, 341.88034188034186, 119.65811965811965, 111.1111111111111))
    args = parser.parse_args()

    odb_path = os.path.abspath(args.odb_path)
    odb = odbAccess.openOdb(path=odb_path, readOnly=True)
    try:
        frame = odb.steps["Load"].frames[-1]
        instance = odb.rootAssembly.instances["SPECIMEN-1"]
        strain_field = frame.fieldOutputs["E"]
        stress_field = frame.fieldOutputs["S"]
        reaction_field = frame.fieldOutputs["RF"]
        nodes = {node.label: tuple(node.coordinates) for node in instance.nodes}
        stresses = {(value.elementLabel, value.integrationPoint): value for value in stress_field.values}
        half_span = args.span_mm / 2.0
        center_half = args.center_width_mm / 2.0
        A = np.zeros((8, 4), dtype=float)
        internal = np.zeros(8, dtype=float)
        element_count = 0
        strain_spans = np.zeros(3, dtype=float)
        for evalue in strain_field.values:
            element = next(item for item in instance.elements if item.label == evalue.elementLabel)
            coords = [nodes[label] for label in element.connectivity]
            centroid = tuple(sum(point[j] for point in coords) / 4.0 for j in (0, 1))
            thickness = args.center_thickness_mm if abs(centroid[0]) <= center_half and abs(centroid[1]) <= center_half else args.arm_thickness_mm
            actual = np.asarray((component(strain_field, evalue, "E11"), component(strain_field, evalue, "E22"), component(strain_field, evalue, "E12")))
            stress_value = stresses[(evalue.elementLabel, evalue.integrationPoint)]
            actual_stress = np.asarray((component(stress_field, stress_value, "S11"), component(stress_field, stress_value, "S22"), component(stress_field, stress_value, "S12")))
            strain_spans = np.maximum(strain_spans, np.abs(actual))
            virtual_strain_integrals = element_virtual_strains(coords, half_span) * thickness
            for index in range(8):
                exs, eys, gys = virtual_strain_integrals[index]
                A[index, :] += np.asarray((actual[0] * exs, actual[1] * eys, actual[0] * eys + actual[1] * exs, actual[2] * gys))
                internal[index] += actual_stress.dot(np.asarray((exs, eys, gys)))
            element_count += 1

        external = np.zeros(8, dtype=float)
        displacement_nodes = 0
        for value in reaction_field.values:
            coords = nodes[value.nodeLabel]
            rf = list(value.data)
            for index, field in enumerate(virtual_fields(coords[0], coords[1], half_span)):
                external[index] += rf[0] * field[0] + rf[1] * field[1]
            if abs(rf[0]) > 0.0 or abs(rf[1]) > 0.0:
                displacement_nodes += 1

        q_true = np.asarray(args.q_true, dtype=float)
        result = {
            "odb_path": odb_path,
            "status": "OPENED_READ_ONLY_RECOMPUTED",
            "element_count": element_count,
            "nonzero_reaction_nodes": displacement_nodes,
            "A_rank": int(np.linalg.matrix_rank(A)),
            "A_condition_number": float(np.linalg.cond(A)),
            "q_true_MPa": q_true.tolist(),
            "external_virtual_work_Nmm": external.tolist(),
            "internal_virtual_work_Nmm": internal.tolist(),
            "external_internal_relative_error": float(np.linalg.norm(external - internal) / max(np.linalg.norm(internal), np.finfo(float).eps)),
            "external_rhs_fit": fit(A, external, q_true),
            "internal_rhs_diagnostic_fit": fit(A, internal, q_true),
            "strain_component_max_abs": strain_spans.tolist(),
            "integration": "CPS4R reduced integration: nodal virtual displacements, bilinear interpolation, and one-point element work",
            "shear_convention": "Abaqus E12 used as exported; no extra factor of 2",
        }
        output_path = os.path.abspath(args.output_json)
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        with open(output_path, "w") as handle:
            json.dump(result, handle, indent=2, sort_keys=True)
        print(json.dumps(result, indent=2, sort_keys=True))
    finally:
        odb.close()


if __name__ == "__main__":
    main()
