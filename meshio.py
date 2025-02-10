import meshio
import sys
for path in sys.argv[1:]:
    print(path)
    mesh = meshio.read(path, file_format="xdmf")
    print(mesh)
