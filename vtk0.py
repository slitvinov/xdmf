import sys
from vtkmodules.vtkCommonCore import VTK_ERROR
from vtkmodules.vtkIOXdmf2 import vtkXdmfReader


path = sys.argv[1]
xr = vtkXdmfReader()
xr.CanReadFile(path)
xr.SetFileName(path)
xr.UpdateInformation()
xr.Update()

ds = xr.GetOutputDataObject(0)
print(f"vtk.py: cell, points: {ds.GetNumberOfCells()}, {ds.GetNumberOfPoints()}")
print(ds)
