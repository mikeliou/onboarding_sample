import xml.etree.ElementTree as ET

root = ET.parse('sample.sdlxliff').getroot()

for node in root.iter():
    if 'seg-source' in node.tag and node.text is not None:
        print(node.text)
