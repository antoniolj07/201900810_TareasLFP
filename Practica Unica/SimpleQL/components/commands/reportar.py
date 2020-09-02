import re
import dominate
from dominate.tags import *
import webbrowser
import os
import datetime

class Reportar:
    registros = []
    def __init__(self, archivo, texto):
        self.archivo = archivo
        self.texto = texto
        fecha = datetime.datetime.now()
        elements = re.split('\s', str(fecha))
        horaTemplet = elements[1]
        self.hora = horaTemplet.replace(':', '-')

        self.ver_cantidad()

    def ver_cantidad(self):
        separados = re.split('\s', self.texto)
        #try:
        self.registros = []
        self.cantidad = int(separados[1])
        for x in range(self.cantidad):
            self.registros.append(self.archivo[x])
        self.crear_pagina()
        #except:
            #print('No se reconoce: ', separados[1])

    def crear_pagina(self):
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
                            th('Promedio')
                    with tbody():
                        for registro in self.registros:
                            with tr():
                                td(registro.nombre)
                                td(registro.activo)
                                td(registro.edad)
                                td(registro.promedio)

        with open('pages/registro'+str(self.hora)+'.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)

        webbrowser.open_new_tab(os.path.abspath('pages/registro'+str(self.hora)+'.html'))


            


