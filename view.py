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
layout = CreateLayout()
layout.AssignView(0, view)
layout.SetSize(*view.ViewSize)
view.EnableRayTracing = 1
view.StereoType = 'Crystal Eyes'
view.OrientationAxesVisibility = 0
xdmf = XDMFReader(FileNames=[xdmf_path])
view.CameraParallelProjection = 1
disp = Show()
disp.SetRepresentationType("Surface With Edges")
Render()
SaveScreenshot(png_path, view)
