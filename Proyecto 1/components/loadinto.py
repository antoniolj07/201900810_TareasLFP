from afd_aon import AfdAon
class LoadInto:
    def __init__(self, mensaje):
        self.afd_load_into(mensaje)

    def afd_load_into(self, mensaje):
        lEst = 0
        selectedSet = ''
        paths = []
        error = False
        for x in range(len(mensaje)):
            if lEst == 0:
                if mensaje[x].lower() in ('l'):
                    lEst = 1
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 1:
                if mensaje[x].lower() in ('o'):
                    lEst = 2
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 2:
                if mensaje[x].lower() in ('a'):
                    lEst = 3
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 3:
                if mensaje[x].lower() in ('d'):
                    lEst = 4
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 4:
                if mensaje[x].lower() in (' '):
                    lEst = 4
                elif mensaje[x].lower() in ('i'):
                    lEst = 5
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 5:
                if mensaje[x].lower() in ('n'):
                    lEst = 6
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 6:
                if mensaje[x].lower() in ('t'):
                    lEst = 7
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 7:
                if mensaje[x].lower() in ('o'):
                    lEst = 8
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 8:
                selectedSet = ''
                if mensaje[x].lower() in (' '):
                    lEst = 8
                elif mensaje[x].isalpha():
                    selectedSet = selectedSet + mensaje[x]
                    lEst = 9
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 9:
                if mensaje[x].isalpha():
                    selectedSet = selectedSet + mensaje[x]
                    lEst = 9
                elif mensaje[x] in (' '):
                    lEst = 10
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 10:
                if mensaje[x] in (' '):
                    lEst = 10
                elif mensaje[x].lower() in ('f'):
                    lEst = 11
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 11:
                if mensaje[x].lower() in ('i'):
                    lEst = 12
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 12:
                if mensaje[x].lower() in ('l'):
                    lEst = 13
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 13:
                if mensaje[x].lower() in ('e'):
                    lEst = 14
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 14:
                if mensaje[x].lower() in ('s'):
                    lEst = 15
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 15:
                nuevoPath = ''
                if mensaje[x] in (' '):
                    lEst = 15
                elif (mensaje[x].isalpha() or mensaje[x] in ('/',':','.') or mensaje[x].isdigit()):
                    nuevoPath = nuevoPath + mensaje[x]
                    lEst = 16
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif lEst == 16:
                if (mensaje[x].isalpha() or mensaje[x] in ('/',':','.') or mensaje[x].isdigit()):
                    nuevoPath = nuevoPath + mensaje[x]
                    lEst = 16
                    if x == len(mensaje) - 1:
                        paths.append(nuevoPath)
                elif mensaje[x] in (','):
                    paths.append(nuevoPath)
                    lEst = 15
                else:
                    error = True
                    print('Entrada invalida')
                    break
        self.error = error
        self.selectedSet = selectedSet
        self.leer_archivos(paths)

    def leer_archivos(self, archivos):
        r = AfdAon(archivos)
        self.registros = r.registros




            
            
