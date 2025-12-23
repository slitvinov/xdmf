#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *BIN_FILE_NAME = "particles.raw";

int main(void) {
  int nver, i;
  const float phi = (1.0f + sqrtf(5.0f)) / 2.0f;
  const float ver[] = {
      -1,  phi, 0,   1,   phi, 0,   -1,   -phi, 0,    1,    -phi, 0,
      0,   -1,  phi, 0,   1,   phi, 0,    -1,   -phi, 0,    1,    -phi,
      phi, 0,   -1,  phi, 0,   1,   -phi, 0,    -1,   -phi, 0,    1,
  };
  FILE *bin_file;
  float *y_attr;

  nver = sizeof ver / sizeof *ver / 3;

  y_attr = malloc(nver * sizeof(float));
  if (y_attr == NULL) {
    fprintf(stderr, "particles.c: Failed to allocate memory for y_attr\n");
    return 1;
  }
  for (i = 0; i < nver; i++) {
    y_attr[i] = ver[3 * i + 1];
  }

  bin_file = fopen(BIN_FILE_NAME, "wb");
  if (bin_file == NULL) {
    fprintf(stderr, "particles.raw.c: error message '%s'\n", strerror(errno));
    return 1;
  }

  fwrite(ver, sizeof(float), 3 * nver, bin_file);
  fwrite(y_attr, sizeof(float), nver, bin_file);

  if (fclose(bin_file) == EOF) {
    fprintf(stderr, "particles.raw.c: error message '%s'\n", strerror(errno));
    free(y_attr);
    return 1;
  }
  free(y_attr);

  printf("<Xdmf\n"
         "    Version=\"2\">\n"
         "  <Domain>\n"
         "    <Grid>\n"
         "      <Topology\n"
         "          TopologyType=\"Polyvertex\"\n"
         "          Dimensions=\"%d\"/>\n"
         "      <Geometry>\n"
         "        <DataItem\n"
         "            Dimensions=\"%d 3\"\n"
         "            Format=\"Binary\">\n"
         "          %s\n"
         "        </DataItem>\n"
         "      </Geometry>\n"
         "      <Attribute\n"
         "          Name=\"y\">\n"
         "        <DataItem\n"
         "            Dimensions=\"%d\"\n"
         "            Seek=\"%ld\"\n"
         "            Format=\"Binary\">\n"
         "          %s\n"
         "        </DataItem>\n"
         "      </Attribute>\n"
         "    </Grid>\n"
         "  </Domain>\n"
         "</Xdmf>\n",
         nver, nver, BIN_FILE_NAME, nver, 3 * nver * sizeof(float),
         BIN_FILE_NAME);

  return 0;
}
