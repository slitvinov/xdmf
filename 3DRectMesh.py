import random
import numpy as np
import sys

xdmf_path = "3DRectMesh.xdmf2"
attr_path = "3DRectMesh.attr.raw"
sx_path = "3DRectMesh.x.raw"
sy_path = "3DRectMesh.y.raw"
sz_path = "3DRectMesh.z.raw"

nx, ny, nz = 10, 20, 30
attr = np.memmap(attr_path,
                 dtype=np.dtype("<f8"),
                 mode="w+",
                 shape=(nx, ny, nz),
                 order="F")
it = np.nditer(attr, ["multi_index"], ["readwrite"])
for x in it:
    i, j, k = it.multi_index
    attr[i, j, k] = i + j + k

sx = np.memmap(sx_path, dtype=np.dtype("<f8"), mode="w+", shape=nx)
sy = np.memmap(sx_path, dtype=np.dtype("<f8"), mode="w+", shape=ny)
sz = np.memmap(sx_path, dtype=np.dtype("<f8"), mode="w+", shape=nz)

with open(xdmf_path, "w") as f:
    f.write(f'''\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
          TopologyType="3DCoRectMesh"
          Dimensions="{nz + 1} {ny + 1} {nx + 1}"/>
      <Geometry
          GeometryType="ORIGIN_DXDYDZ">
        <DataItem
            Format="Binary"
            Precision="8"
            Dimensions="{nx + 1}">
          {sx_path}
        </DataItem>
        <DataItem
            Format="Binary"
            Precision="8"
            Dimensions="{ny + 1}">
          {sy_path}
        </DataItem>
        <DataItem
            Format="Binary"
            Precision="8"
            Dimensions="{nz + 1}">
          {sz_path}
        </DataItem>
      </Geometry>
      <Attribute
          Center="Cell"
          Name="u">
        <DataItem
            Format="Binary"
            Precision="8"
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
''')
