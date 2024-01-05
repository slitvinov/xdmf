import struct
import random

xdmf_path = "a.xdmf2"
xyz_path = "a.xyz.raw"

n = 10
with open(xdmf_path, "w") as f:
    f.write("""\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
	  TopologyType="Polyvertex"/>
      <Geometry>
	<DataItem
	    Dimensions="%ld 3"
	    Format="Binary">
          %s
	</DataItem>
      </Geometry>
    </Grid>
  </Domain>
</Xdmf>
""" % (n, xyz_path))

with open(xyz_path, "wb") as f:
    for i in range(3 * n):
        x = random.random()
        f.write(struct.pack("f", x))
