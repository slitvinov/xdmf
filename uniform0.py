import random
import numpy as np

xdmf_path = "a.xdmf2"
attr_path = "a.attr.raw"

nx, ny, nz = 10, 20, 30
attr = np.memmap(attr_path,
                 dtype=np.uint8,
                 mode="w+",
                 shape=(nx, ny, nz),
                 order="F")
it = np.nditer(attr, ["multi_index"], ["readwrite"])
for x in it:
    i, j, k = it.multi_index
    x.itemset(i < j)
with open(xdmf_path, "w") as f:
    f.write("""\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
          TopologyType="3DCoRectMesh"
          Dimensions="%ld %ld %ld"/>
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
            NumberType="UChar"
            Dimensions="%ld %ld %ld">
          %s
        </DataItem>
      </Attribute>
    </Grid>
  </Domain>
</Xdmf>
""" % (nz + 1, ny + 1, nx + 1, nz, ny, nx, attr_path))
