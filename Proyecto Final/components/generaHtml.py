from token import Token
import dominate
from dominate.tags import *
import webbrowser
import os

class GeneraHtml:
    tokens = []
    def __init__(self, tokens, errores):
        self.tokensHtml(tokens, errores)

    def tokensHtml(self, tokens, errores):
        for token in tokens:
            tkn = Token(token['lexema'], token['token'], token['descripcion'], token['linea'], token['columna'])
            if token['lexema'] == 'true':
                token['token'] = 'tkn_true'
                token['descripcion'] = 'palabra reservada true'
            elif token['lexema'] == 'false':
                token['token'] = 'tkn_false'
                token['descripcion'] = 'palabra reservada false'

            self.tokens.append(token)
            
        for token in self.tokens:
            print('{} === {} === {} === {} === {}'.format(token['lexema'], token['token'], token['descripcion'], token['linea'], token['columna']))


        doc = dominate.document(title = 'tokensHtml')
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        
        with doc:
            with div( cls='container mt-5 mb-5'):
                h1('List Tokens')
                hr()
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Lexema')
                            th('Token')
                            th('Descripcion')
                            th('Linea')
                            th('Columna')
                    with tbody():
                        for token in self.tokens:
                            with tr():
                                td(token['lexema'])
                                td(token['token'])
                                td(token['descripcion'])
                                td(token['linea'])
                                td(token['columna'])

        with open('pages/tokensHtml.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)
        webbrowser.open_new_tab(os.path.abspath('pages/tokensHtml.html'))



        errorDoc = dominate.document(title = 'erroresHtml')
        with errorDoc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        
        with errorDoc:
            with div( cls='container mt-5 mb-5'):
                h1('List Errors')
                hr()
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Linea')
                            th('Columna')
                    with tbody():
                        for error in errores:
                            with tr():
                                td(error['linea'])
                                td(error['columna'])

        with open('pages/erroresHtml.html', 'wb') as errFile:
            errb = errorDoc.render().encode()
            errFile.write(errb)
        webbrowser.open_new_tab(os.path.abspath('pages/erroresHtml.html'))