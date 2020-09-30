from createset import CreateSet
from count import Count
from loadinto import LoadInto
from useset import UseSet
from select import Select
from listattributes import ListAttributes
from printin import PrintIn
from mini import Min
from maxi import Max
from suma import Suma
from script import Script
from reportafd import Report
class Menu:
    entrada = ''
    comandos = ['create set', 'load into', 'use set', 'select', 'list attributes', 'print in', 'max', 'min', 'sum', 'count', 'report to', 'script', 'report tokens']

    def __init__(self):
        self.afd()

    def afd(self):
        self.sets = []
        self.setUsing = {}
        print('===> Bienvenido a SimpleQL CLIT <===')
        while self.entrada != 'salir':
            entrada = ''
            mensaje = input()
            estado = 0
            for x in range(len(mensaje)):
                if estado == 0:
                    if mensaje[x].lower() in ('c'):
                        estado = 1
                    elif mensaje[x].lower() in ('l'):
                        estado = 2
                    elif mensaje[x].lower() in ('u'):
                        estado = 3
                    elif mensaje[x].lower() in ('s'):
                        estado = 4
                    elif mensaje[x].lower() in ('p'):
                        estado = 5
                    elif mensaje[x].lower() in ('m'):
                        estado = 6
                    elif mensaje[x].lower() in ('r'):
                        estado = 7
                    elif mensaje[x] in (' '):
                        estado = 0
                    else:
                        print('Entrada invalida')
                        break
                elif estado == 1:
                    if mensaje[x].lower() in ('r'):
                        cs = CreateSet(mensaje)
                        if not cs.error:
                            new = True
                            for s in self.sets:
                                if s['idSet'] == cs.nSet['idSet']:
                                    new = False
                            if new:
                                self.sets.append(cs.nSet)
                                print('Nuevo set {} creado'.format(cs.nSet['idSet']))
                            else:
                                print('Ya existe un set con el nombre: ',cs.nSet['idSet'])
                        break
                            
                    elif mensaje[x].lower() in ('o'):
                        coun = Count(mensaje)
                        break
                    else:
                        print('Entrada invalida')
                        break
                elif estado == 2:
                    if mensaje[x].lower() in ('o'):
                        lInto = LoadInto(mensaje)
                        if not lInto.error:
                            resultado = False
                            for s in self.sets:
                                if s['idSet'] == lInto.selectedSet:
                                    s['archivos'] = lInto.registros
                                    resultado = True
                                    print('Archivos cargados en: ', s['idSet'])        
                                    print(s)
                            if not resultado:
                                print('No se encontro set: ',lInto.selectedSet)
                        break
                    elif mensaje[x].lower() in ('i'):
                        lAtt = ListAttributes(mensaje, 'set')
                        break
                    else:
                        print('Entrada invalida')
                        break
                elif estado == 3:
                    uset = UseSet(mensaje)
                    if not uset.error:
                        haySet = False
                        for i in range(len(self.sets)):
                            if self.sets[i]['idSet'] == uset.uset:
                                self.indice = i
                                haySet = True
                        if haySet:
                            print('Usando set: ',self.sets[self.indice]['idSet'])
                        else:
                            print('No se encontro set con nombre: ', uset.uset)
                            self.indice = -1
                    break
                elif estado == 4:
                    if mensaje[x].lower() in ('e'):
                        sel = Select(mensaje)
                        break
                    elif mensaje[x].lower() in ('u'):
                        su = Suma(mensaje)
                        break
                    elif mensaje[x].lower() in ('c'):
                        sc = Script(mensaje)
                        break
                    else:
                        print('Entrada invalida')
                        break
                elif estado == 5:
                    pi = PrintIn(mensaje)
                    break
                elif estado == 6:
                    if mensaje[x].lower() in ('a'):
                        ma = Max(mensaje)
                        break
                    elif mensaje[x].lower() in ('i'):
                        mi = Min(mensaje)
                        break
                elif estado == 7:
                    re = Report(mensaje)
                    break
                else:
                    print('Entrada invalida')
                    break

m = Menu()
#report to html select nombre, apellido where edad = 45 and promedio > 75