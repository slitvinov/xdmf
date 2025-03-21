import sys
import re
from vtkmodules.vtkIOXdmf2 import vtkXdmfReader
from vtkmodules.vtkCommonDataModel import VTK_TRIANGLE
try:
    path = sys.argv[1]
except IndexError:
    sys.stderr.write(f"vtk.py: error: need an XDF file\n")
    exit(1)
xr = vtkXdmfReader()
if not xr.CanReadFile(path):
    sys.stderr.write(f"vtk.py: error: cannot read '{path}'\n")
    exit(1)
xr.SetFileName(path)
xr.SetDebug(True)
xr.UpdateInformation()
for i in range(xr.GetNumberOfGrids()):
    name = xr.GetGridName(i)
    print(f"vtk.py: GetGridName: {name}")
for i in range(xr.GetNumberOfCellArrays()):
    print(f"vtk.py: cell array: {xr.GetCellArrayName(i)}")
for i in range(xr.GetNumberOfPointArrays()):
    print(f"vtk.py: point array: {xr.GetPointArrayName(i)}")
xr.Update()
for i in range(xr.GetNumberOfOutputPorts()):
    ds = xr.GetOutputDataObject(i)
    if hasattr(ds, "GetPoints"):
        points = ds.GetPoints()
        print(
            f"vtk.py: cell, points: {ds.GetNumberOfCells()}, {ds.GetNumberOfPoints()}"
        )
        for j in range(ds.GetNumberOfCells()):
            if ds.GetCellType(j) == VTK_TRIANGLE:
                cell = ds.GetCell(j)
                ids = [
                    cell.GetPointId(j) for j in range(cell.GetNumberOfPoints())
                ]
                print(f"Triangle {j}: Point IDs {ids}")
                coordinates = [points.GetPoint(pid) for pid in ids]
                print(f"Triangle {j}: Coordinates {coordinates}")
ds = xr.GetOutputDataObject(0)
print(f"vtk.py: cell, points: {ds.GetNumberOfCells()}, {ds.GetNumberOfPoints()}")
print(ds)

