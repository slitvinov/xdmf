import sys

x0 = 1
y0 = 2
z0 = 3

lx = 1
ly = 2
lz = 3

path = "box.xdmf2"
with open(path, "w") as f:
    f.write(f'''\
<Xdmf
    Version="2">
  <Domain>
    <Grid>
      <Topology
          TopologyType="3DCoRectMesh"
          Dimensions="2 2 2"/>
      <Geometry
          GeometryType="ORIGIN_DXDYDZ">
        <DataItem
            Dimensions="3">
          {z0:.16e}
          {y0:.16e}
          {x0:.16e}
        </DataItem>
        <DataItem
            Dimensions="3">
          {lz:.16e}
          {ly:.16e}
          {lx:.16e}
        </DataItem>
      </Geometry>
    </Grid>
  </Domain>
</Xdmf>
''')
sys.stderr.write(f"box.py: {path}\n")
