#include <math.h>
#include <stdio.h>

int main(void) {
  int nver, i;
  const double phi = (1.0 + sqrt(5.0)) / 2.0;
  const double ver[] = {
    -1.0,  phi,  0.0,
     1.0,  phi,  0.0,
    -1.0, -phi,  0.0,
     1.0, -phi,  0.0,
     0.0, -1.0,  phi,
     0.0,  1.0,  phi,
     0.0, -1.0, -phi,
     0.0,  1.0, -phi,
     phi,  0.0, -1.0,
     phi,  0.0,  1.0,
    -phi,  0.0, -1.0,
    -phi,  0.0,  1.0,
};
  nver = sizeof ver / sizeof *ver / 3;
  printf(
"<Xdmf\n"\
"    Version=\"2\">\n"\
"  <Domain>\n"\
"    <Grid>\n"\
"      <Topology\n"\
"	  TopologyType=\"Polyvertex\"\n"\
"	  Dimensions=\"%d\">\n"\
"      </Topology>\n"\
"      <Geometry>\n"\
"	<DataItem\n"\
"	    Dimensions=\"%d 3\"\n"\
"	    Format=\"XML\">\n",
nver, nver);
  for (i = 0; i < 3 * nver; i++)
    printf("          %+.16e\n", ver[i]);
    printf(
"	</DataItem>\n"\
"      </Geometry>\n"\
"      <Attribute\n"\
"	  Name=\"y\">\n"\
"	<DataItem\n"\
"	    Dimensions=\"%d\"\n"\
"	    Format=\"XML\">\n", nver);
  for (i = 0; i < nver; i++)
    printf("          %+.16e\n", ver[3 * i + 1]);
    printf(
"	</DataItem>\n"\
"      </Attribute>\n"\
"    </Grid>\n"\
"  </Domain>\n"\
"</Xdmf>\n");
}
