import paraview
from paraview.simple import *
import sys

png_path = "npy.png"
png_size = 800, 600
xdmf_path = "npy.xdmf2"

renderView1 = CreateView('RenderView')
renderView1.ViewSize = png_size
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [5.0, 10.0, 15.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-40.521315740304956, 13.404734378557393, -15.435958943611285]
renderView1.CameraFocalPoint = [19.452263981984927, 8.91905321216619, 24.6629129901986]
renderView1.CameraViewUp = [0.10285349426433193, 0.9937812105178928, -0.042662212075897064]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 18.708286933869708
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]
SetActiveView(None)
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(*png_size)
SetActiveView(renderView1)
npyxdmf2 = XDMFReader(FileNames=[xdmf_path])
npyxdmf2.CellArrayStatus = ['u']
outline1 = Outline(registrationName='Outline1', Input=npyxdmf2)
npyxdmf2Display = Show(npyxdmf2, renderView1, 'UniformGridRepresentation')
uTF2D = GetTransferFunction2D('u')
uTF2D.ScalarRangeInitialized = 1
uTF2D.Range = [0.0, 57.0, 0.0, 1.0]
uLUT = GetColorTransferFunction('u')
uLUT.TransferFunction2D = uTF2D
uLUT.RGBPoints = [0.0, 0.0, 0.0, 0.5625, 6.333327000000001, 0.0, 0.0, 1.0, 20.8095315, 0.0, 1.0, 1.0, 28.0476195, 0.5, 1.0, 0.5, 35.2857075, 1.0, 1.0, 0.0, 49.761912, 1.0, 0.0, 0.0, 57.0, 0.5, 0.0, 0.0]
uLUT.ColorSpace = 'RGB'
uLUT.ScalarRangeInitialized = 1.0
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 57.0, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1
npyxdmf2Display.Representation = 'Volume'
npyxdmf2Display.ColorArrayName = ['CELLS', 'u']
npyxdmf2Display.LookupTable = uLUT
npyxdmf2Display.SelectTCoordArray = 'None'
npyxdmf2Display.SelectNormalArray = 'None'
npyxdmf2Display.SelectTangentArray = 'None'
npyxdmf2Display.OSPRayScaleFunction = 'PiecewiseFunction'
npyxdmf2Display.SelectOrientationVectors = 'None'
npyxdmf2Display.ScaleFactor = 3.0
npyxdmf2Display.SelectScaleArray = 'u'
npyxdmf2Display.GlyphType = 'Arrow'
npyxdmf2Display.GlyphTableIndexArray = 'u'
npyxdmf2Display.GaussianRadius = 0.15
npyxdmf2Display.SetScaleArray = [None, '']
npyxdmf2Display.ScaleTransferFunction = 'PiecewiseFunction'
npyxdmf2Display.OpacityArray = [None, '']
npyxdmf2Display.OpacityTransferFunction = 'PiecewiseFunction'
npyxdmf2Display.DataAxesGrid = 'GridAxesRepresentation'
npyxdmf2Display.PolarAxes = 'PolarAxesRepresentation'
npyxdmf2Display.ScalarOpacityUnitDistance = 2.059113413569457
npyxdmf2Display.ScalarOpacityFunction = uPWF
npyxdmf2Display.TransferFunction2D = uTF2D
npyxdmf2Display.OpacityArrayName = ['CELLS', 'u']
npyxdmf2Display.ColorArray2Name = ['CELLS', 'u']
npyxdmf2Display.IsosurfaceValues = [28.5]
npyxdmf2Display.SliceFunction = 'Plane'
npyxdmf2Display.Slice = 15
npyxdmf2Display.SelectInputVectors = [None, '']
npyxdmf2Display.WriteLog = ''

# init the 'Plane' selected for 'SliceFunction'
npyxdmf2Display.SliceFunction.Origin = [5.0, 10.0, 15.0]

# show data from outline1
outline1Display = Show(outline1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
outline1Display.Representation = 'Surface'
outline1Display.AmbientColor = [0.0, 0.0, 0.0]
outline1Display.ColorArrayName = [None, '']
outline1Display.DiffuseColor = [0.0, 0.0, 0.0]
outline1Display.LineWidth = 10.0
outline1Display.SelectTCoordArray = 'None'
outline1Display.SelectNormalArray = 'None'
outline1Display.SelectTangentArray = 'None'
outline1Display.OSPRayScaleFunction = 'PiecewiseFunction'
outline1Display.SelectOrientationVectors = 'None'
outline1Display.ScaleFactor = 3.0
outline1Display.SelectScaleArray = 'None'
outline1Display.GlyphType = 'Arrow'
outline1Display.GlyphTableIndexArray = 'None'
outline1Display.GaussianRadius = 0.15
outline1Display.SetScaleArray = [None, '']
outline1Display.ScaleTransferFunction = 'PiecewiseFunction'
outline1Display.OpacityArray = [None, '']
outline1Display.OpacityTransferFunction = 'PiecewiseFunction'
outline1Display.DataAxesGrid = 'GridAxesRepresentation'
outline1Display.PolarAxes = 'PolarAxesRepresentation'
outline1Display.SelectInputVectors = [None, '']
outline1Display.WriteLog = ''
SetActiveSource(outline1)
SaveScreenshot(png_path, renderView1)
