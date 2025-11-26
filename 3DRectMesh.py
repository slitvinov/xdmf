import random
import numpy as np
import sys

xdmf_path = "3DRectMesh.xdmf2"
attr_path = "3DRectMesh.attr.raw"
sx_path = "3DRectMesh.x.raw"
sy_path = "3DRectMesh.y.raw"
sz_path = "3DRectMesh.z.raw"

nx, ny, nz = 10, 20, 30
dtype = np.dtype("<f8")
precision = dtype.itemsize
attr = np.memmap(attr_path,
                 dtype=dtype,
                 mode="w+",
                 shape=(nx, ny, nz),
                 order="F")
it = np.nditer(attr, ["multi_index"], ["readwrite"])
for x in it:
    i, j, k = it.multi_index
    attr[i, j, k] = i + j + k

sx = np.memmap(sx_path, dtype=dtype, mode="w+", shape=nx + 1)
sy = np.memmap(sy_path, dtype=dtype, mode="w+", shape=ny + 1)
sz = np.memmap(sz_path, dtype=dtype, mode="w+", shape=nz + 1)

beta = 2.0
coeff = beta / np.tanh(beta)
sx[:] = np.arange(nx + 1)
sy[:] = ny * np.tanh(coeff * np.linspace(0.0, 1.0, ny + 1))
sz[:] = nz * np.tanh(coeff * np.linspace(0.0, 1.0, nz + 1))

with open(xdmf_path, "w") as f:
    f.write(f'''\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
          TopologyType="3DRectMesh"
          Dimensions="{nz + 1} {ny + 1} {nx + 1}"/>
      <Geometry
          GeometryType="VXVYVZ">
        <DataItem
            Format="Binary"
            Precision="{precision}"
            Dimensions="{nx + 1}">
          {sx_path}
        </DataItem>
        <DataItem
            Format="Binary"
            Precision="{precision}"
            Dimensions="{ny + 1}">
          {sy_path}
        </DataItem>
        <DataItem
            Format="Binary"
            Precision="{precision}"
            Dimensions="{nz + 1}">
          {sz_path}
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
3DRectMesh.py: {attr_path=}
3DRectMesh.py: {xdmf_path=}
3DRectMesh.py: {sx_path=}
3DRectMesh.py: {sy_path=}
3DRectMesh.py: {sz_path=}
''')
