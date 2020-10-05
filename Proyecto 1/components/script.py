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
from reportafd import Report
class Script:
    def __init__(self, mensaje, sets, indice):
        self.sets = sets
        self.indice = indice
        self.afd_script(mensaje)
    def afd_script(self, mensaje):
        sEst = 0
        error = False
        paths = []
        for x in range(len(mensaje)):
            if sEst == 0:
                if mensaje[x].lower() in ('s'):
                    sEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 1:
                if mensaje[x].lower() in ('c'):
                    sEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 2:
                if mensaje[x].lower() in ('r'):
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 3:
                if mensaje[x].lower() in ('i'):
                    sEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 4:
                if mensaje[x].lower() in ('p'):
                    sEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 5:
                if mensaje[x].lower() in ('t'):
                    sEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 6:
                path = ''
                if mensaje[x].lower() in (' '):
                    sEst = 6
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('/',':','.'):
                    path = path + mensaje[x]
                    if x == len(mensaje) - 1:
                        paths.append(path)
                    sEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 7:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('/',':','.'):
                    path = path + mensaje[x]
                    if x == len(mensaje) - 1:
                        paths.append(path)
                    sEst = 7
                elif mensaje[x] in (','):
                    paths.append(path)
                    sEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
        if not error:
            print(paths)
            self.readSript(paths)
            
    def readSript(self, paths):
        if len(paths) > 0:
            for path in paths:
                contenido = ''
                try:
                    with open(path, 'r') as f:
                        lineas = f.readlines()
                    for linea in lineas:
                        contenido = contenido + linea.strip()
                except:
                    print('No se pudo leer el archivo ', path)

            comandos = []
            comando = ''
            entreComillas = False
            for x in range(len(contenido)):
                if not contenido[x] in (';'):
                    if contenido[x] in ('\"') and not entreComillas:
                        entreComillas = True
                    elif contenido[x] in ('\"') and entreComillas:
                        entreComillas = False
                    comando = comando + contenido[x]
                elif contenido[x] in (';') and entreComillas:
                    comando = comando + contenido[x]
                else:
                    comandos.append(comando)
                    comando = ''
            print(comandos)

            for com in comandos:
                estado = 0
                for x in range(len(com)):
                    if estado == 0:
                        if com[x].lower() in ('c'):
                            estado = 1
                        elif com[x].lower() in ('l'):
                            estado = 2
                        elif com[x].lower() in ('u'):
                            estado = 3
                        elif com[x].lower() in ('s'):
                            estado = 4
                        elif com[x].lower() in ('p'):
                            estado = 5
                        elif com[x].lower() in ('m'):
                            estado = 6
                        elif com[x].lower() in ('r'):
                            estado = 7
                        elif com[x] in (' '):
                            estado = 0
                        else:
                            print('Entrada invalida')
                            break
                    elif estado == 1:
                        if com[x].lower() in ('r'):
                            cs = CreateSet(com)
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
                                
                        elif com[x].lower() in ('o'):
                            if self.indice != -1:
                                coun = Count(com, self.sets[self.indice])
                            else:
                                print('No se ha seleccionado ningun set')    
                            break
                        else:
                            print('Entrada invalida')
                            break
                    elif estado == 2:
                        if com[x].lower() in ('o'):
                            lInto = LoadInto(com)
                            if not lInto.error:
                                resultado = False
                                for s in self.sets:
                                    if s['idSet'] == lInto.selectedSet:
                                        s['archivos'] = lInto.registros
                                        s['atributos'] = lInto.atributos
                                        resultado = True
                                        print('Archivos cargados en: ', s['idSet'])        
                                        print(s)
                                if not resultado:
                                    print('No se encontro set: ',lInto.selectedSet)
                            break
                        elif com[x].lower() in ('i'):
                            if self.indice != -1:
                                lAtt = ListAttributes(com, self.sets[self.indice])
                            else:
                                print('No se ha elejido ningun set')
                            break
                        else:
                            print('Entrada invalida')
                            break
                    elif estado == 3:
                        uset = UseSet(com)
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
                        if com[x].lower() in ('e'):
                            if self.indice != -1:
                                sel = Select(com, self.sets[self.indice])
                            else:
                                print('No se ha seleccionado ningun set')
                            break
                        elif com[x].lower() in ('u'):
                            if self.indice != -1:
                                su = Suma(com, self.sets[self.indice])
                            else:
                                print('No se ha seleccionado ningun set')    
                            break
                        else:
                            print('Entrada invalida')
                            break
                    elif estado == 5:
                        pi = PrintIn(com)
                        break
                    elif estado == 6:
                        if com[x].lower() in ('a'):
                            if self.indice != -1:
                                ma = Max(com, self.sets[self.indice])
                            else:
                                print('No se ha seleccionado ningun set')
                            break
                        elif com[x].lower() in ('i'):
                            if self.indice != -1:
                                mi = Min(com, self.sets[self.indice])
                            else:
                                print('No se ha seleccionado ningun set')
                            break
                    elif estado == 7:
                        if self.indice != -1:
                            re = Report(com, self.sets[self.indice])
                        else:
                            print('No se ha seleccionado ningun set')
                        break
                    else:
                        print('Entrada invalida')
                        break



