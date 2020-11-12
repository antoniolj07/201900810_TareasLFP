from token import Token
import dominate
from dominate.tags import *
import webbrowser
import os
class Graph:
    def __init__(self, bloques):
        self.bloques = bloques
        self.generarHtml()

    def generarHtml(self):
        bloques = self.bloques
        doc = dominate.document(title = 'diagrama')
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
            title('Diagrama de Flujo')
            script(src="https://kit.fontawesome.com/91179a3f5d.js", crossorigin="anonymous")
        with doc:
            with div( cls='m-5'):
                h1('Flujo de Script')
                hr()
                with div(cls="row"):
                    with div(style="width: 60%;margin-right: auto; margin-left: auto;"):
                        with div(cls="text-center", style="width: 20%;height: 50px;margin-right: auto; margin-left: auto; border-radius: 50%;border: 3px solid black;"):
                            with div():
                                h5('Inicio')

                with div(cls="row"):
                    with div(style="width: 3%;margin-right: auto; margin-left: auto;"):
                        i(cls="fas fa-long-arrow-alt-down fa-5x", style="margin-right: auto; margin-left: auto;") 

                x = 1
                for bloque in bloques:
                    with div(cls="row"):
                        with div(style="width: 60%;margin-right: auto; margin-left: auto;"):
                            with div(cls="card border-secondary mb-3", style="max-width: 18rem;width: 18rem;margin-right: auto; margin-left: auto;"):
                                with div(cls="card-header"):
                                    if bloque['nombre'] == ('Sentencia If') or bloque['nombre'] == ('Sentencia While'):
                                        print('por que putas')
                                        h5(bloque['nombre']+', Condicion: '+bloque['parametros'][0])
                                    elif bloque['nombre'] in ('asignacion') or bloque['nombre'] in ('definicion'):
                                        if len(bloque['parametros']) > 0:
                                            parametros = ''
                                            for para in bloque['parametros']:
                                                parametros = parametros + para + ', '
                                            h5(bloque['nombre'] + ': '+bloque['identificador'] + ', Parametros: '+ parametros)
                                        else:
                                            h5(bloque['nombre'] + ': '+bloque['identificador'])
                                    elif bloque['nombre'] in ('Llamada'):
                                        parametros = ''
                                        for para in bloque['parametros']:
                                            parametros = parametros + para + ', '
                                        if len(bloque['parametros']) > 0:
                                            h5(bloque['nombre'] + ': '+ bloque['identificador'] + ', parametros: ' + parametros)
                                        else: 
                                            h5(bloque['nombre'] + ': '+ bloque['identificador'])
                                    elif bloque['nombre'] in ('Sentencia Foreach'):
                                        h5(bloque['nombre'] + ', Elemento: '+bloque['parametros'][0]+' de '+bloque['parametros'][1])
                                    
                                    elif bloque['nombre'] in ('Sentencia Switch'):
                                        h5(bloque['nombre']+' con identificador '+bloque['parametros'][0])
                                if len(bloque['contenido']) > 0:
                                    with ul(cls="list-group list-group-flush"):
                                        for nbloc in bloque['contenido']:
                                            with li(cls="list-group-item"):
                                                if nbloc['nombre'] in ('Sentencia If') or nbloc['nombre'] in ('Sentencia While'):
                                                    label(nbloc['nombre']+', Condicion: '+nbloc['parametros'][0])
                                                elif nbloc['nombre'] in ('asignacion') or nbloc['nombre'] in ('definicion'):
                                                    if len(nbloc['parametros']) > 0:
                                                        parametros = ''
                                                        for para in nbloc['parametros']:
                                                            parametros = parametros + para + ', '
                                                        label(nbloc['nombre'] + ': '+nbloc['identificador'] + ', Parametros: '+ parametros)
                                                    else:
                                                        label(nbloc['nombre'] + ': '+nbloc['identificador'])
                                                elif nbloc['nombre'] in ('Llamada'):
                                                    parametros = ''
                                                    for para in nbloc['parametros']:
                                                        parametros = parametros + para + ', '
                                                    if len(nbloc['parametros']) > 0:
                                                        label(nbloc['nombre'] + ': '+ nbloc['identificador'] + ', parametros: ' + parametros)
                                                    else:
                                                        label(nbloc['nombre']+': '+nbloc['identificador'])
                                                elif nbloc['nombre'] in ('Sentencia Foreach'):
                                                    label(nbloc['nombre'] + ', Elemento: '+nbloc['parametros'][0]+' de '+nbloc['parametros'][1])
                                                
                                                elif nbloc['nombre'] in ('Case'):
                                                    label(nbloc['nombre']+' '+nbloc['parametros'][0]+': ')
                                                elif nbloc['nombre'] in ('Default'):
                                                    label(nbloc['nombre']+': ')
                                                
                                                if len(nbloc['contenido']) > 0:
                                                    with div(cls="alert alert-secondary"):
                                                        with ul():
                                                            for newbloc in nbloc['contenido']:
                                                                with li():
                                                                    if newbloc['nombre'] in ('Sentencia If') or newbloc['nombre'] in ('Sentencia While'):
                                                                        label(newbloc['nombre']+', Condicion: '+newbloc['parametros'][0])
                                                                    elif newbloc['nombre'] in ('asignacion') or newbloc['nombre'] in ('definicion'):
                                                                        if len(newbloc['parametros']) > 0:
                                                                            parametros = ''
                                                                            for para in newbloc['parametros']:
                                                                                parametros = parametros + para + ', '
                                                                            label(newbloc['nombre'] + ': '+newbloc['identificador'] + ', Parametros: '+ parametros)
                                                                        else:
                                                                            label(newbloc['nombre'] + ': '+newbloc['identificador'])
                                                                    elif newbloc['nombre'] in ('Llamada'):
                                                                        parametros = ''
                                                                        for para in newbloc['parametros']:
                                                                            parametros = parametros + para + ', '
                                                                        if len(newbloc['parametros']) > 0:
                                                                            label(newbloc['nombre'] + ': '+ newbloc['identificador'] + ', parametros: ' + parametros)
                                                                        else:
                                                                            label(newbloc['nombre']+': '+newbloc['identificador'])
                                                                    elif newbloc['nombre'] in ('Sentencia Foreach'):
                                                                        label(newbloc['nombre'] + ', Elemento: '+newbloc['parametros'][0]+' de '+newbloc['parametros'][1])
                    with div(cls="row"):
                        with div(style="width: 3%;margin-right: auto; margin-left: auto;"):
                            i(cls="fas fa-long-arrow-alt-down fa-5x", style="margin-right: auto; margin-left: auto;")                                               
                    x = x + 1

        with open('pages/diagrama_flujo.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)
        webbrowser.open_new_tab(os.path.abspath('pages/diagrama_flujo.html'))


