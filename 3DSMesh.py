import random
import numpy as np
import sys

xdmf_path = "3DSMesh.xdmf2"
attr_path = "3DSMesh.attr.raw"
point_path = "3DSMesh.point.raw"

nx, ny, nz = 10, 20, 30
dtype = np.dtype("<f8")
precision = dtype.itemsize
attr = np.memmap(attr_path,
                 dtype=dtype,
                 mode="w+",
                 shape=(nx, ny, nz),
                 order="F")
point = np.memmap(point_path, dtype=dtype, mode="w+", shape=(3, nx + 1, ny + 1, nz + 1), order="F")
it = np.nditer(attr, ["multi_index"], ["readwrite"])
for x in it:
    i, j, k = it.multi_index
    attr[i, j, k] = i + j + k
# Add curvature to coordinates
curvature_x = 0.1  # Adjust for more/less curvature
curvature_y = 0.1
curvature_z = 0.1
for k in range(nz + 1):
    for j in range(ny + 1):
        for i in range(nx + 1):
            # Normalized coordinates [0, 1]
            u = i / nx if nx > 0 else 0
            v = j / ny if ny > 0 else 0
            w = k / nz if nz > 0 else 0
            # Add curved distortion
            point[0, i, j, k] = i + curvature_x * np.sin(2 * np.pi * v) * np.sin(2 * np.pi * w)
            point[1, i, j, k] = j + curvature_y * np.sin(2 * np.pi * u) * np.sin(2 * np.pi * w)
            point[2, i, j, k] = k + curvature_z * np.sin(2 * np.pi * u) * np.sin(2 * np.pi * v)
with open(xdmf_path, "w") as f:
    f.write(f'''\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
          TopologyType="3DSMesh"
          Dimensions="{nz + 1} {ny + 1} {nx + 1}"/>
      <Geometry
          GeometryType="XYZ">
        <DataItem
            Format="Binary"
            Precision="{precision}"
            Dimensions="{nz + 1} {ny + 1} {nx + 1} 3">
          {point_path}
        </DataItem>
      </Geometry>
      <Attribute
          Center="Cell"
          Name="u">
        <DataItem
            Format="Binary"
            Precision="{precision}"
            Dimensions="{nz} {ny} {nx}">
          {attr_path}
        </DataItem>
      </Attribute>
    </Grid>
  </Domain>
</Xdmf>
''')
sys.stderr.write(f'''\
3DSMesh.py: {attr_path=}
3DSMesh.py: {xdmf_path=}
3DSMesh.py: {point_path=}
''')
