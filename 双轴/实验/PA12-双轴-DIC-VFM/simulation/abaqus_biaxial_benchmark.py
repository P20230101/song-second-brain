"""Abaqus/CAE 2025 可运行的二维平面应力双轴基准。

这是软件链路验证模型，不代表用户试样几何或 PA12 实测参数。单位 N、mm、MPa。
在 Abaqus/CAE 中通过 File -> Run Script 执行。
"""
from abaqus import *
from abaqusConstants import *
import regionToolset, mesh, odbAccess, os, csv, json

root = r"D:\松的第二大脑\松的第二大脑\双轴\实验\PA12-双轴-DIC-VFM\simulation"
if not os.path.isdir(root):
    os.makedirs(root)
name = "PA12_Biaxial_Benchmark_20260915"
model = mdb.models[name] if name in mdb.models else mdb.Model(name=name)

sk = model.ConstrainedSketch(name="plate_profile", sheetSize=200.0)
sk.rectangle(point1=(0.0, 0.0), point2=(100.0, 100.0))
part = model.Part(name="Plate", dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
part.BaseShell(sketch=sk)
del model.sketches[sk.name]

mat = model.Material(name="PA12_benchmark_elastic")
mat.Elastic(table=((300.0, 0.35),))
model.HomogeneousSolidSection(name="Section", material=mat.name, thickness=2.0)
part.SectionAssignment(region=regionToolset.Region(faces=part.faces[:]), sectionName="Section")

elem = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
part.setElementType(regions=(part.faces,), elemTypes=(elem,))
part.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
part.generateMesh()

asm = model.rootAssembly
inst = asm.Instance(name="Plate-1", part=part, dependent=ON)
left = inst.edges.getByBoundingBox(xMin=-1e-6, xMax=1e-6, yMin=-1.0, yMax=101.0)
right = inst.edges.getByBoundingBox(xMin=99.999999, xMax=100.000001, yMin=-1.0, yMax=101.0)
bottom = inst.edges.getByBoundingBox(xMin=-1.0, xMax=101.0, yMin=-1e-6, yMax=1e-6)
top = inst.edges.getByBoundingBox(xMin=-1.0, xMax=101.0, yMin=99.999999, yMax=100.000001)
model.StaticStep(name="Load", previous="Initial", nlgeom=OFF)
model.DisplacementBC(name="FixX", createStepName="Initial", region=regionToolset.Region(edges=left), u1=0.0)
model.DisplacementBC(name="FixY", createStepName="Initial", region=regionToolset.Region(edges=bottom), u2=0.0)
model.DisplacementBC(name="PullX", createStepName="Load", region=regionToolset.Region(edges=right), u1=0.5)
model.DisplacementBC(name="PullY", createStepName="Load", region=regionToolset.Region(edges=top), u2=0.5)
model.fieldOutputRequests["F-Output-1"].setValues(variables=("U", "S", "E"))

jobName = name
if jobName in mdb.jobs:
    del mdb.jobs[jobName]
mdb.Job(name=jobName, model=name, type=ANALYSIS, description="synthetic biaxial plane-stress benchmark")
mdb.jobs[jobName].submit(consistencyChecking=OFF)
mdb.jobs[jobName].waitForCompletion()

odb = odbAccess.openOdb(path=os.path.join(root, jobName + ".odb"), readOnly=True)
frame = odb.steps["Load"].frames[-1]
with open(os.path.join(root, "nodal_displacement.csv"), "w") as f:
    w = csv.writer(f); w.writerow(("node_label", "x0_mm", "y0_mm", "u_mm", "v_mm"))
    for v in frame.fieldOutputs["U"].values:
        n = odb.rootAssembly.instances["PLATE-1"].getNodeFromLabel(v.nodeLabel)
        w.writerow((v.nodeLabel, n.coordinates[0], n.coordinates[1], v.data[0], v.data[1]))
with open(os.path.join(root, "element_strain_stress.csv"), "w") as f:
    w = csv.writer(f); w.writerow(("element_label", "integration_point", "exx", "eyy", "gxy", "s11", "s22", "s12"))
    efield = frame.fieldOutputs["E"].values; sfield = frame.fieldOutputs["S"].values
    for e, s in zip(efield, sfield):
        ed = list(e.data) + [0.0] * 3; sd = list(s.data) + [0.0] * 3
        w.writerow((e.elementLabel, e.integrationPoint, ed[0], ed[1], ed[2], sd[0], sd[1], sd[2]))
meta = {"source": "synthetic", "model": "plane_stress_CPS4R", "E_MPa": 300.0, "nu": 0.35, "thickness_mm": 2.0, "ux_right_mm": 0.5, "uy_top_mm": 0.5, "job": jobName}
with open(os.path.join(root, "abaqus_benchmark_manifest.json"), "w") as f:
    json.dump(meta, f, indent=2)
odb.close()
print("PA12 Abaqus benchmark completed: " + root)
