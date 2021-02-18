import xml.etree.ElementTree as ET
from lxml import etree

root = etree.parse('C:\\Users\\mlc\\Downloads\\sample.sdlxliff')

find = etree.XPath("//*[local-name()='seg-source']")
#text = find_text(root)[0]
for node in find(root):
    if node.text:
        print(node.text)

