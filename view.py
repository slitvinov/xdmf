import sys

sys.argv.pop(0)
if sys.argv:
    xdmf_path = sys.argv.pop(0)
    png_path = sys.argv.pop(0)
else:
    xdmf_path = "icosahedron.xdmf2"
    png_path = "icosahedron.png"
import paraview
from paraview.simple import *

size = 400, 300
view = CreateView("RenderView")
view.ViewSize = size
view.OrientationAxesVisibility = 0
view.CameraParallelProjection = 1
view.Background = 1, 1, 1
layout = CreateLayout()
layout.AssignView(0, view)
layout.SetSize(*view.ViewSize)
xdmf = OpenDataFile(xdmf_path)
disp = Show()
if xdmf.CellData.NumberOfArrays:
    disp.SetRepresentationType("Surface With Edges")
    ColorBy(disp, ('CELLS', 'y'))
else:
    disp.SetRepresentationType("Point Gaussian")
    disp.GaussianRadius = 0.5
    ColorBy(disp, ('POINTS', 'y'))
Render()
SaveScreenshot(png_path, view)
