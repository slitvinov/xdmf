#!/bin/env pvbatch

import paraview
from paraview.simple import *
import sys

png_path = "npy.png"
png_size = 400, 300
xdmf_path = "npy.xdmf2"

view = CreateView('RenderView')
view.ViewSize = png_size
view.OrientationAxesVisibility = 0
view.CenterOfRotation = 5.0, 10.0, 15.0
view.CameraPosition = -41, 13, -15
view.CameraFocalPoint = 19, 9, 25
view.CameraViewUp = 0.1, 1, 0
view.UseColorPaletteForBackground = 0
view.Background = 1.0, 1.0, 1.0
layout = CreateLayout()
xdmf2 = XDMFReader(FileNames=[xdmf_path])
xdmf2.CellArrayStatus = ['u']
outline = Outline(Input=xdmf2)
xdmf2Display = Show(xdmf2, view, 'UniformGridRepresentation')
uTF2D = GetTransferFunction2D('u')
uTF2D.ScalarRangeInitialized = 1
uTF2D.Range = [0.0, 57.0, 0.0, 1.0]
uLUT = GetColorTransferFunction('u')
uLUT.TransferFunction2D = uTF2D
uLUT.RGBPoints = [
    0.0, 0.0, 0.0, 0.5625, 6.333327000000001, 0.0, 0.0, 1.0, 20.8095315, 0.0,
    1.0, 1.0, 28.0476195, 0.5, 1.0, 0.5, 35.2857075, 1.0, 1.0, 0.0, 49.761912,
    1.0, 0.0, 0.0, 57.0, 0.5, 0.0, 0.0
]
uLUT.ColorSpace = 'RGB'
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 57.0, 1.0, 0.5, 0.0]
xdmf2Display.Representation = 'Volume'
xdmf2Display.ColorArrayName = ['CELLS', 'u']
xdmf2Display.LookupTable = uLUT
xdmf2Display.ScalarOpacityFunction = uPWF
outlineDisplay = Show(outline, view, 'GeometryRepresentation')
outlineDisplay.DiffuseColor = [0.0, 0.0, 0.0]
outlineDisplay.LineWidth = 5
SaveScreenshot(png_path, view)
