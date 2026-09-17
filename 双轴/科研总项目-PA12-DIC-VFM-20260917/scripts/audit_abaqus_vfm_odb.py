"""Read-only acceptance audit for an Abaqus ODB used by the VFM benchmark.

Run with the Abaqus Python interpreter. The script does not modify the ODB;
it writes a small JSON audit result so the Gate 3/4 decision is reproducible.
"""
from __future__ import print_function

import argparse
import json
import math
import os
import statistics

import odbAccess


def values_for(field, label):
    index = field.componentLabels.index(label)
    return [float(value.data[index]) for value in field.values]


def mean_abs(values):
    return sum(abs(value) for value in values) / float(len(values)) if values else 0.0


def span(values):
    return max(values) - min(values) if values else 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("odb_path")
    parser.add_argument("output_json")
    args = parser.parse_args()

    odb_path = os.path.abspath(args.odb_path)
    odb = odbAccess.openOdb(path=odb_path, readOnly=True)
    try:
        step_names = list(odb.steps.keys())
        if "Load" not in odb.steps:
            raise ValueError("ODB lacks the expected Load step")
        step = odb.steps["Load"]
        if not step.frames:
            raise ValueError("Load step has no frames")
        frame = step.frames[-1]
        required = ("U", "S", "E", "RF")
        missing = [name for name in required if name not in frame.fieldOutputs]
        if missing:
            raise ValueError("ODB lacks required field outputs: " + ",".join(missing))

        instance_names = list(odb.rootAssembly.instances.keys())
        strain = frame.fieldOutputs["E"]
        stress = frame.fieldOutputs["S"]
        displacement = frame.fieldOutputs["U"]
        reaction = frame.fieldOutputs["RF"]
        exx = values_for(strain, "E11")
        eyy = values_for(strain, "E22")
        gxy = values_for(strain, "E12")
        s11 = values_for(stress, "S11")
        s22 = values_for(stress, "S22")
        s12 = values_for(stress, "S12")
        rf1 = values_for(reaction, "RF1")
        rf2 = values_for(reaction, "RF2")

        # Independent virtual-work figures are read from the existing extractor
        # output for the same job, when available. They are not reconstructed
        # from a fitted parameter vector here.
        job_name = os.path.splitext(os.path.basename(odb_path))[0]
        sibling = os.path.join(os.path.dirname(os.path.dirname(odb_path)), "fields")
        vfm_json = os.path.join(sibling, job_name + "_vfm.json")
        vfm = None
        if os.path.isfile(vfm_json):
            with open(vfm_json, "r") as handle:
                vfm = json.load(handle)
        external = vfm.get("external_virtual_work_Nmm", []) if vfm else []
        internal = vfm.get("internal_virtual_work_Nmm", []) if vfm else []
        work_error = None
        if external and internal and len(external) == len(internal):
            denominator = max(math.sqrt(sum(value * value for value in internal)), 1.0e-30)
            work_error = math.sqrt(sum((a - b) * (a - b) for a, b in zip(external, internal))) / denominator

        result = {
            "odb_path": odb_path,
            "open_status": "OPENED_READ_ONLY",
            "step_names": step_names,
            "load_frame_count": len(step.frames),
            "last_frame_value": float(frame.frameValue),
            "instance_names": instance_names,
            "required_field_outputs": required,
            "field_output_counts": {name: len(frame.fieldOutputs[name].values) for name in required},
            "displacement_components": list(displacement.componentLabels),
            "reaction_components": list(reaction.componentLabels),
            "reaction_mean_abs": {"RF1": mean_abs(rf1), "RF2": mean_abs(rf2)},
            "reaction_sum": {"RF1": sum(rf1), "RF2": sum(rf2)},
            "strain_span": {"E11": span(exx), "E22": span(eyy), "E12": span(gxy)},
            "stress_span": {"S11": span(s11), "S22": span(s22), "S12": span(s12)},
            "strain_std": {"E11": statistics.pstdev(exx) if exx else 0.0,
                            "E22": statistics.pstdev(eyy) if eyy else 0.0,
                            "E12": statistics.pstdev(gxy) if gxy else 0.0},
            "virtual_work_external_internal_relative_error": work_error,
            "vfm_json_path": os.path.abspath(vfm_json) if vfm else None,
            "physical_field_gate": {
                "required_outputs_present": not missing,
                "nonzero_reaction": bool(mean_abs(rf1) > 0.0 or mean_abs(rf2) > 0.0),
                "heterogeneous_strain": bool(any(span(values) > 1.0e-12 for values in (exx, eyy, gxy))),
                "virtual_work_available": work_error is not None,
            },
        }
        result["physical_field_gate"]["all_basic_checks_pass"] = all(result["physical_field_gate"].values())
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
