import math
import sys

phi = (1 + math.sqrt(5)) / 2
ver = [
    [-1, phi, 0],
    [1, phi, 0],
    [-1, -phi, 0],
    [1, -phi, 0],
    [0, -1, phi],
    [0, 1, phi],
    [0, -1, -phi],
    [0, 1, -phi],
    [phi, 0, -1],
    [phi, 0, 1],
    [-phi, 0, -1],
    [-phi, 0, 1],
]

tri = [
    [0, 11, 5],
    [0, 5, 1],
    [0, 1, 7],
    [0, 7, 10],
    [0, 10, 11],
    [1, 5, 9],
    [5, 11, 4],
    [11, 10, 2],
    [10, 7, 6],
    [7, 1, 8],
    [3, 9, 4],
    [3, 4, 2],
    [3, 2, 6],
    [3, 6, 8],
    [3, 8, 9],
    [4, 9, 5],
    [2, 4, 11],
    [6, 2, 10],
    [8, 6, 7],
    [9, 8, 1],
]

ver_str = '\n          '.join(' '.join(f"{x:+.16e}" for x in row)
                              for row in ver)
tri_str = '\n          '.join(' '.join(f"{x:2d}" for x in row) for row in tri)

with open(sys.argv[1], "w") as file:
    file.write(f'''\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
	  TopologyType="Triangle"
	  Dimensions="{len(tri)}">
	<DataItem
	    Dimensions="{len(tri)} 3"
	    NumberType="Int"
	    Format="XML">
          {tri_str}
	</DataItem>
      </Topology>
      <Geometry>
	<DataItem
	    Dimensions="{len(ver)} 3"
	    Format="XML">
          {ver_str}
	</DataItem>
      </Geometry>
    </Grid>
  </Domain>
</Xdmf>
''')
