import dominate
from dominate.tags import *
import webbrowser
import os

class ReportTokens:
    def __init__(self, mensaje, nset={}):
        self.afd_report_tokens(mensaje)
    
    def afd_report_tokens(self, mensaje):
        rEst = 0
        error = False
        for x in range(len(mensaje)):
            if rEst == 0:
                if mensaje[x].lower() in ('r'):
                    rEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 1:
                if mensaje[x].lower() in ('e'):
                    rEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 2:
                if mensaje[x].lower() in ('p'):
                    rEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 3:
                if mensaje[x].lower() in ('o'):
                    rEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 4:
                if mensaje[x].lower() in ('r'):
                    rEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 5:
                if mensaje[x].lower() in ('t'):
                    rEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 6:
                if mensaje[x] in (' '):
                    rEst = 6
                elif mensaje[x].lower() in ('t'):
                    rEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 7:
                if mensaje[x].lower() in ('o'):
                    rEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 8:
                if mensaje[x].lower() in ('k'):
                    rEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 9:
                if mensaje[x].lower() in ('e'):
                    rEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 10:
                if mensaje[x].lower() in ('n'):
                    rEst = 11
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 11:
                if mensaje[x].lower() in ('s'):
                    rEst = 12
                else:
                    print('Entrada invalida')
                    error = True
                    break
        if not error:
            self.report()

    def report(self):
        contenido = [
            {
                'Lexema': 'Create',
                'Nombre': 'tk_create',
                'descripcion': 'Crea el nuevo set'
            },{
                'Lexema': 'Set',
                'Nombre': 'tk_set',
                'descripcion': 'Hace referencia a que se quiere crear un nuevo set'
            },{
                'Lexema': 'Load',
                'Nombre': 'tk_load',
                'descripcion': 'Cargar algo en un archivo'
            },{
                'Lexema': 'Into',
                'Nombre': 'tk_into',
                'descripcion': 'En cual set se quiere cargar los archivos'
            },{
                'Lexema': 'Files',
                'Nombre': 'tk_files',
                'descripcion': 'Se quiere cargar los archivos'
            },{
                'Lexema': 'Use',
                'Nombre': 'tk_use',
                'descripcion': 'Que set se quiere utilizar'
            },{
                'Lexema': 'Select',
                'Nombre': 'tk_select',
                'descripcion': 'Seleccionar atributos de un set'
            },{
                'Lexema': 'Where',
                'Nombre': 'tk_where',
                'descripcion': 'Seleccionar atributos donde exista una coincidencia'
            },{
                'Lexema': 'And',
                'Nombre': 'tk_and',
                'descripcion': 'Cuando se debe cumplir dos condiciones'
            },{
                'Lexema': 'Or',
                'Nombre': 'tk_or',
                'descripcion': 'Cuando se debe cumplir una o las dos condiciones'
            },{
                'Lexema': 'Xor',
                'Nombre': 'tk_xor',
                'descripcion': 'Cuando se debe cumplir solamente una de las dos condiciones'
            },{
                'Lexema': 'Count',
                'Nombre': 'tk_count',
                'descripcion': 'Contar la cantidad de atributos que no son null'
            },{
                'Lexema': '*',
                'Nombre': 'tk_*',
                'descripcion': 'Se hace referencia a todos los atributos de los registros'
            },{
                'Lexema': 'Max',
                'Nombre': 'tk_max',
                'descripcion': 'Se quiere saber el valor maximo de un atributo'
            },{
                'Lexema': 'Min',
                'Nombre': 'tk_min',
                'descripcion': 'Se quiere saber el valor minimo de un atributo de todos los registro'
            },{
                'Lexema': 'Sum',
                'Nombre': 'tk_sum',
                'descripcion': 'La suma total de cierto atributo de todos los registros'
            },{
                'Lexema': 'Report',
                'Nombre': 'tk_report',
                'descripcion': 'Reportar informacion'
            },{
                'Lexema': 'To',
                'Nombre': 'tk_to',
                'descripcion': 'Reportar informacion en un lugar en especifico'
            },{
                'Lexema': 'tokens',
                'Nombre': 'tk_tokens',
                'descripcion': 'Se desea reportar los tokens del proyecto'
            },{
                'Lexema': 'List',
                'Nombre': 'tk_list',
                'descripcion': 'Se desea listar algo'
            },{
                'Lexema': 'Attributes',
                'Nombre': 'tk_attributes',
                'descripcion': 'Cuando se debe cumplir solamente una de las dos condiciones'
            },{
                'Lexema': 'Print',
                'Nombre': 'tk_print',
                'descripcion': 'Imprimir mensajes en la consola'
            },{
                'Lexema': 'In',
                'Nombre': 'tk_in',
                'descripcion': 'Se desea imprimir en algun color'
            },{
                'Lexema': 'Red',
                'Nombre': 'tk_red',
                'descripcion': 'Color rojo'
            },{
                'Lexema': 'Blue',
                'Nombre': 'tk_blue',
                'descripcion': 'Color azul'
            },{
                'Lexema': 'Green',
                'Nombre': 'tk_green',
                'descripcion': 'Color verde'
            },{
                'Lexema': 'Orange',
                'Nombre': 'tk_orange',
                'descripcion': 'Color naranja'
            },{
                'Lexema': 'Yellow',
                'Nombre': 'tk_yellow',
                'descripcion': 'Color amarillo'
            },{
                'Lexema': 'Pink',
                'Nombre': 'tk_pink',
                'descripcion': 'Color rosa'
            },
        ]
        doc = dominate.document(title = 'Report_Tokens')
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        with doc:
            with div( cls='container mt-5 mb-5'):
                h1('List Attributes')
                hr()
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Lexema')
                            th('Nombre')
                            th('Descripcion')
                    with tbody():
                        for registro in contenido:
                            with tr():
                                td(registro['Lexema'])
                                td(registro['Nombre'])
                                td(registro['descripcion'])
        with open('pages/Report_Tokens.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)
        webbrowser.open_new_tab(os.path.abspath('pages/Report_Tokens.html'))
