import dominate
from dominate.tags import *
import webbrowser
import os
import datetime
import re

class Main:
    data = [{
        'nombre': 'Jorge',
        'edad': 20,
        'activo': True,
        'saldo': 2500
    },
    {
        'nombre': 'Antonio',
        'edad': 19,
        'activo': False,
        'saldo': 3500
    },
    {
        'nombre': 'Javier',
        'edad': 25,
        'activo': True,
        'saldo': 4000
    },
    {
        'nombre': 'Andres',
        'edad': 27,
        'activo': False,
        'saldo': 2450
    },
    {
        'nombre': 'Andrea',
        'edad': 19,
        'activo': True,
        'saldo': 5000
    },
    {
        'nombre': 'Bony',
        'edad': 20,
        'activo': False,
        'saldo': 10000
    },
    {
        'nombre': 'Sofia',
        'edad': 30,
        'activo': True,
        'saldo': 4000
    },
    {
        'nombre': 'Oscar',
        'edad': 31,
        'activo': False,
        'saldo': 15000
    },
    {
        'nombre': 'Nicolle',
        'edad': 23,
        'activo': True,
        'saldo': 6000
    },
    {
        'nombre': 'Sebastain',
        'edad': 35,
        'activo': False,
        'saldo': 2900
    }]
    def __init__(self):
        self.create_html()

    def create_html(self):
        fecha = datetime.datetime.now()
        elements = re.split('\s', str(fecha))
        horaTemplet = elements[1]
        self.hora = horaTemplet.replace(':', '-')

        doc = dominate.document(title = 'Registros')
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        with doc:
            with div( cls='container mt-5 mb-5'):
                h1('Registros')
                hr()
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Nombre')
                            th('Activo')
                            th('Edad')
                            th('Saldo')
                    with tbody():
                        for registro in self.data:
                            with tr():
                                td(registro.get('nombre'))
                                td(registro.get('activo'))
                                td(registro.get('edad'))
                                td(registro.get('saldo'))

        with open('pages/registro'+str(self.hora)+'.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)

        webbrowser.open_new_tab(os.path.abspath('pages/registro'+str(self.hora)+'.html'))

main = Main()