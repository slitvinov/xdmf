import random
import numpy as np
import sys

xdmf_path = "npy.xdmf2"
attr_path = "npy.attr.npy"

nx, ny, nz = 10, 20, 30
attr = np.empty((nx, ny, nz), order="F")
it = np.nditer(attr, ["multi_index"], ["readwrite"])
for x in it:
    i, j, k = it.multi_index
    x.itemset(i + j + k)

np.save(attr_path, attr.T)
with open(attr_path, "rb") as f:
    offset = 0
    while True:
        c = f.read(1)
        offset += 1
        if c == b'\n':
            break

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
            Dimensions="3">
          0
          0
          0
        </DataItem>
        <DataItem
            Dimensions="3">
          1
          1
          1
        </DataItem>
      </Geometry>
      <Attribute
          Center="Cell"
          Name="u">
        <DataItem
            Format="Binary"
            Precision="8"
            Seek="{offset}"
            Dimensions="{nz} {ny} {nx}">
          {attr_path}
        </DataItem>
      </Attribute>
    </Grid>
  </Domain>
</Xdmf>
''')
sys.stderr.write(f'''\
npy.py: {offset=}
npy.py: {attr_path=}
npy.py: {xdmf_path=}
''')
