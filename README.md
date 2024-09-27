<h2>XDMF examples</h2>

<h3>Validation</h3>

<pre>
$ python valid.py Xdmf.dtd *.xdmf2
</pre>

<h3>TopologyType<h3>

Linear:
[Polyvertex](polyvertex.xdmf2),
[Polyline](polyline.xdmf2),
[Polygon](polygon.xdmf2),
[Triangle](triangle.xdmf2),
[Hexahedron](hexahedron.xdmf2)
[Quadrilateral](quadrilateral.xdmf2)

Arbitrary:
[Mixed](mixed.xdmf2)

Quadratic:
[Edge_3](edge_3.xdmf2),
[Tri_3](triangle_6.xdmf2)

Structured:
[3DCoRectMesh](3dcorectmesh.xdmf2)

[Use NPY format](npy.py), [read XDFM file using VTK library](vtk.py):

<pre>
$ python vtk.py 3dcorectmesh.xdmf2
vtk.py: cell, points: 6, 24
</pre>


<h3>References</h3>

1. Mark, E. "Enhancements to the extensible data model and format (xdmf)." 2007 DoD High Performance Computing Modernization Program Users Group Conference. IEEE, 2007. <https://apps.dtic.mil/sti/tr/pdf/ADP023792.pdf>
2. <https://www.xdmf.org/index.php/XDMF_Model_and_Format>
3. [VisIt User Manual](https://visit-sphinx-github-user-manual.readthedocs.io/en/task-allen-vtk9_master_ospray/data_into_visit/XdmfFormat.html)
4. [vtkXdmfReader](https://vtk.org/doc/nightly/html/classvtkXdmfReader.html)
3. <https://gitlab.kitware.com/xdmf/xdmf>
