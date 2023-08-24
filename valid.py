import sys
import lxml
import lxml.etree

try:
    path = sys.argv[1]
    dtd = lxml.etree.DTD(path)
except lxml.etree.DTDParseError as msg:
    sys.stderr.write("valid.py: %s: %s\n" % (path, msg))
    sys.exit(1)
except IndexError as msg:
    sys.stderr.write("valid.py: error: needs a DTD file\n")
    sys.exit(1)

for path in sys.argv[2:]:
    parser = lxml.etree.XMLParser()
    try:
        tree = lxml.etree.parse(path, parser)
    except OSError:
        sys.stderr.write("valid.py: error: not a file '%s'\n" % path)
        sys.exit(1)
    if not dtd.validate(tree):
        for e in dtd.error_log.filter_from_errors():
            print(e)
