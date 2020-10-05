class ListAttributes:
    def __init__(self, mensaje, selectedSet):
        self.nset = selectedSet
        self.afd_list_attributes(mensaje)

    def afd_list_attributes(self, mensaje):
        lEst = 0
        error = False
        for x in range(len(mensaje)):
            if lEst == 0:
                if mensaje[x].lower() in ('l'):
                    lEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 1:
                if mensaje[x].lower() in ('i'):
                    lEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 2:
                if mensaje[x].lower() in ('s'):
                    lEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 3:
                if mensaje[x].lower() in ('t'):
                    lEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 4:
                if mensaje[x] in (' '):
                    lEst = 4
                elif mensaje[x].lower() in ('a'):
                    lEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 5:
                if mensaje[x].lower() in ('t'):
                    lEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 6:
                if mensaje[x].lower() in ('t'):
                    lEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 7:
                if mensaje[x].lower() in ('r'):
                    lEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 8:
                if mensaje[x].lower() in ('i'):
                    lEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 9:
                if mensaje[x].lower() in ('b'):
                    lEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 10:
                if mensaje[x].lower() in ('u'):
                    lEst = 11
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 11:
                if mensaje[x].lower() in ('t'):
                    lEst = 12
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 12:
                if mensaje[x].lower() in ('e'):
                    lEst = 13
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 13:
                if mensaje[x].lower() in ('s'):
                    lEst = 14
                else:
                    print('Entrada invalida')
                    error = True
                    break
        self.error = error
        if not error:
            self.verAtributos()

    def verAtributos(self):
        atributos = list(dict.fromkeys(self.nset['atributos']))
        self.atributos = atributos
        print('ATRUBUTOS:')
        for x in atributos:
            print(x)



