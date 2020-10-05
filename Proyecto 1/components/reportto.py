import dominate
from dominate.tags import *
import webbrowser
import os


from select import Select
from maxi import Max
from mini import Min
from reporttokens import ReportTokens
from listattributes import ListAttributes
from count import Count
from suma import Suma
class ReportTo:
    def __init__(self, mensaje, nset):
        self.nset = nset
        self.afd_report_to(mensaje)
    
    def afd_report_to(self, mensaje):
        rEst = 0
        error = False
        self.nombre = ''
        comando = ''
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
                self.nombre = ''
                if mensaje[x] in (' '):
                    rEst = 8
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('!','@','#','$','%','^','&','*','(',')','_'):
                    self.nombre = self.nombre + mensaje[x]
                    rEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 9:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('!','@','#','$','%','^','&','*','(',')','_'):
                    self.nombre = self.nombre + mensaje[x]
                    rEst = 9
                elif mensaje[x] in (' '):
                    rEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 10:
                i = x
                while i < len(mensaje):
                    comando = comando + mensaje[i]
                    i = i + 1
                if mensaje[x].lower() in ('s'):
                    rEst = 11
                elif mensaje[x].lower() in ('l'):
                    li = ListAttributes(comando, self.nset)
                    if not li.error:
                        self.crearArchivo(li.atributos, 'listattributes')
                    break
                elif mensaje[x].lower() in ('m'):
                    rEst = 12
                elif mensaje[x].lower() in ('c'):
                    c = Count(comando, self.nset)
                    if not c.error:
                        self.crearArchivo(c.cuentas, 'count')
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 11:
                if mensaje[x].lower() in ('e'):
                    se = Select(comando, self.nset)
                    if not se.error:
                        self.crearArchivo(se.resultados, 'select')
                    break
                elif mensaje[x].lower() in ('u'):
                    su = Suma(comando, self.nset)
                    if not su.error:
                        self.crearArchivo(su.sumas, 'suma')
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 12:
                if mensaje[x].lower() in ('a'):
                    ma = Max(comando, self.nset)
                    if not ma.error:
                        self.crearArchivo(ma.maxAtri, 'max', ma.atributo)
                    break
                elif mensaje[x].lower() in ('i'):
                    mi = Min(comando, self.nset)
                    if not mi.error:
                        self.crearArchivo(mi.minAtri, 'min', mi.atributo)
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            else:
                print('Entrada invalida')
                error = True
                break
        
    
    def crearArchivo(self, contenido, tipo, atributo=''):
        doc = dominate.document(title = self.nombre)
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        if tipo in ('listattributes'):
            with doc:
                with div( cls='container mt-5 mb-5'):
                    h1('List Attributes')
                    hr()
                    with table(cls = 'table'):
                        with thead(cls = 'thead-dark'):
                            with tr():
                                th('Atributos')
                        with tbody():
                            for atributo in contenido:
                                with tr():
                                    td(atributo)
        elif tipo in ('count'):
            keys = []
            for key in contenido.keys():
                keys.append(key)
            with doc:
                with div( cls='container mt-5 mb-5'):
                    h1('Count')
                    hr()
                    with table(cls = 'table'):
                        with thead(cls = 'thead-dark'):
                            with tr():
                                for k in keys:
                                    th(k)
                        with tbody():
                            with tr():
                                for k in keys:
                                    td(contenido[k])
        elif tipo in ('select'):
            keys = []
            for key in contenido[0].keys():
                keys.append(key)
            with doc:
                with div( cls='container mt-5 mb-5'):
                    h1('Select')
                    hr()
                    with table(cls = 'table'):
                        with thead(cls = 'thead-dark'):
                            with tr():
                                for k in keys:
                                    th(k)
                        with tbody():
                            for registro in contenido:
                                with tr():
                                    for k in keys:
                                        td(registro[k])  
        elif tipo in ('suma'):
            keys = []
            for key in contenido.keys():
                keys.append(key)
            with doc:
                with div( cls='container mt-5 mb-5'):
                    h1('Sum')
                    hr()
                    with table(cls = 'table'):
                        with thead(cls = 'thead-dark'):
                            with tr():
                                for k in keys:
                                    th(k)
                        with tbody():
                            with tr():
                                for k in keys:
                                    td(contenido[k])
        elif tipo in ('max'):
            with doc:
                with div( cls='container mt-5 mb-5'):
                    h1('Max')
                    hr()
                    with table(cls = 'table'):
                        with thead(cls = 'thead-dark'):
                            with tr():
                                th(atributo)
                        with tbody():
                            with tr():
                                td(contenido)
        elif tipo in ('min'):
            with doc:
                with div( cls='container mt-5 mb-5'):
                    h1('Min')
                    hr()
                    with table(cls = 'table'):
                        with thead(cls = 'thead-dark'):
                            with tr():
                                th(atributo)
                        with tbody():
                            with tr():
                                td(contenido)

        with open('pages/'+self.nombre+'.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)
        webbrowser.open_new_tab(os.path.abspath('pages/'+self.nombre+'.html'))