from xml.dom import minidom

document = minidom.Document()
authorsElement = document.createElement('authors')

datasource = open('../files/cf79.xml')
parsed = minidom.parse(datasource)

authors = parsed.getElementsByTagName('AUTHOR')

for author in authors:
    authorName = author.firstChild.nodeValue

    authorElement = document.createElement('author').nodeValue = authorName
    authorsElement.appendChild(authorElement)
