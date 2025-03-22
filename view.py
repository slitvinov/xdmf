import sys

sys.argv.pop(0)

if sys.argv:
    xdmf_path = sys.argv.pop(0)
    png_path = sys.argv.pop(0)
else:
    xdmf_path = "triangle.xdmf2"
    png_path = "triangle.png"

import paraview
from paraview.simple import *

size = 600, 600
xdmf = XDMFReader(FileNames=[xdmf_path])
view = CreateView("RenderView")
layout = CreateLayout()
layout.AssignView(0, view)
layout.SetSize(size)
view.ViewSize = size
view.EnableRayTracing = 1
view.StereoType = 'Crystal Eyes'
view.OrientationAxesVisibility = 0
view.CameraParallelProjection = 1
view.ResetCamera(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
Show()
Render()
SaveScreenshot(png_path, view)
