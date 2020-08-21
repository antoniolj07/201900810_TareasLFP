import json

print('heroes marvel')

with open('data\heroes-marvel.json') as data:
    contenido = json.loads(data.read())
    for heroe in contenido['heroes_marvel']:
        nombre = heroe.get('nombre')
        poder = heroe.get('poder')
        apodo = heroe.get('apodo')
        debilidad = heroe.get('debilidad')

        print('-----------------------')
        print('nombre: ', nombre)
        print('poder: ', poder)
        print('apodo: ', apodo)
        print('debilidad: ', debilidad)
        print('------------------------')
import main
main.Main()