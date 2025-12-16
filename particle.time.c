#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_TIMESTEPS 100
#define ROTATION_ANGLE_INCREMENT_DEG 5.0f

const char *BIN_FILE_NAME = "particles.raw";

int main(void) {
  int nver, i, t;
  const float phi = (1.0f + sqrtf(5.0f)) / 2.0f;
  float master_ver[] = {
      -1,  phi, 0,   1,   phi, 0,   -1,   -phi, 0,    1,    -phi, 0,
      0,   -1,  phi, 0,   1,   phi, 0,    -1,   -phi, 0,    1,    -phi,
      phi, 0,   -1,  phi, 0,   1,   -phi, 0,    -1,   -phi, 0,    1,
  };
  float ver[sizeof(master_ver) / sizeof(float)];
  FILE *bin_file;
  float *y_attr;

  nver = sizeof master_ver / sizeof *master_ver / 3;

  y_attr = malloc(nver * sizeof(float));
  if (y_attr == NULL) {
    fprintf(stderr, "particle.time.c: Failed to allocate memory for y_attr\n");
    return 1;
  }
  for (i = 0; i < nver; i++) {
    y_attr[i] = master_ver[3 * i + 1];
  }

  bin_file = fopen(BIN_FILE_NAME, "wb");
  if (bin_file == NULL) {
    fprintf(stderr, "particle.time.c: error message '%s' for file %s\n",
            strerror(errno), BIN_FILE_NAME);
    free(y_attr);
    return 1;
  }

  fwrite(y_attr, sizeof(float), nver, bin_file);

  printf("<Xdmf\n"
         "    Version=\"2\">\n"
         "  <Domain>\n"
         "    <Grid\n"
         "        GridType=\"Collection\"\n"
         "        CollectionType=\"Temporal\">\n");

  float current_rotation_angle = 0.0f;
  for (t = 0; t < NUM_TIMESTEPS; ++t) {
    float angle_rad = current_rotation_angle * (M_PI / 180.0f);
    float cos_a = cosf(angle_rad);
    float sin_a = sinf(angle_rad);

    for (i = 0; i < nver; ++i) {
      float x = master_ver[i * 3 + 0];
      float y = master_ver[i * 3 + 1];
      float z = master_ver[i * 3 + 2];
      ver[i * 3 + 0] = x * cos_a - y * sin_a;
      ver[i * 3 + 1] = x * sin_a + y * cos_a;
      ver[i * 3 + 2] = z;
    }

    long int coords_seek_offset = (nver * sizeof(float)) * (1 + 3 * t);
    fwrite(ver, sizeof(float), 3 * nver, bin_file);

    printf("      <Grid>\n"
           "        <Time\n"
           "            Value=\"%d\"/>\n"
           "        <Topology\n"
           "            TopologyType=\"Polyvertex\"\n"
           "            Dimensions=\"%d\"/>\n"
           "        <Geometry\n"
           "            GeometryType=\"XYZ\">\n"
           "          <DataItem\n"
           "              Dimensions=\"%d 3\"\n"
           "              Seek=\"%ld\"\n"
           "              Format=\"Binary\">\n"
           "            %s\n"
           "          </DataItem>\n"
           "        </Geometry>\n"
           "        <Attribute Name=\"y\">\n"
           "          <DataItem\n"
           "              Dimensions=\"%d\"\n"
           "              Format=\"Binary\">\n"
           "            %s\n"
           "          </DataItem>\n"
           "        </Attribute>\n"
           "      </Grid>\n",
           t, nver, nver, coords_seek_offset, BIN_FILE_NAME, nver,
           BIN_FILE_NAME);

    current_rotation_angle += ROTATION_ANGLE_INCREMENT_DEG;
  }

  printf("    </Grid>\n"
         "  </Domain>\n"
         "</Xdmf>\n");
  if (fclose(bin_file) == EOF) {
    fprintf(stderr, "particle.time.c: error message '%s' for file %s\n",
            strerror(errno), BIN_FILE_NAME);
    free(y_attr);
    return 1;
  }
  free(y_attr);
  return 0;
}
