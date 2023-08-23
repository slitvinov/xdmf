import sys
from lxml import etree
dtd = etree.DTD(sys.argv[1])

for path in sys.argv[2:]:
    parser = etree.XMLParser()
    tree = etree.parse(path, parser)
    if not dtd.validate(tree):
        for e in dtd.error_log.filter_from_errors():
            print(e)

