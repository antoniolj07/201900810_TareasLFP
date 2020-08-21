from xml.dom import minidom

print('heroes dc')
docXML = minidom.parse('data\heroes-dc.xml')

heroes = docXML.getElementsByTagName('heroe')

for heroe in heroes:
    name = heroe.getElementsByTagName('nombre')[0]
    poder = heroe.getElementsByTagName('poder')[0]
    apodo = heroe.getElementsByTagName('apodo')[0]
    archinemesis = heroe.getElementsByTagName('archinemesis')[0]

    print('-----------------------------')
    print('nombre: ', name.firstChild.data)
    print('poder: ',poder.firstChild.data)
    print('apodo: ',apodo.firstChild.data)
    print('archinemesis: ',archinemesis.firstChild.data)
    print('-----------------------------')
import main
main.Main()