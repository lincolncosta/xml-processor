import xml.etree.ElementTree as ET

tree = ET.parse('../files/cf79.xml')
root = tree.getroot()

titlesRoot = ET.Element("titles")

for child in root.findall('.//TITLE'):
    authorName = child.text
    ET.SubElement(titlesRoot, "title").text = authorName

titlesTree = ET.ElementTree(titlesRoot)
titlesTree.write("../files/titles.xml")