from xml.dom import minidom

document = minidom.Document()
authorsElement = document.createElement('authors')
document.appendChild(authorsElement)

datasource = open('../files/cf79.xml')
parsed = minidom.parse(datasource)

authors = parsed.getElementsByTagName('AUTHOR')

for author in authors:
    authorName = author.firstChild.nodeValue

    authorElement = document.createElement('author')
    authorNameElement = document.createTextNode(authorName)
    authorElement.appendChild(authorNameElement)

    authorsElement.appendChild(authorElement)

with open('../files/authors.xml', 'w') as out:
    document.writexml(out, encoding='utf-8')
