class ListAttributes:
    def __init__(self, mensaje, selectedSet):
        self.afd_list_attributes(mensaje)

    def afd_list_attributes(self, mensaje):
        lEst = 0
        error = False
        for x in range(len(mensaje)):
            if lEst == 0:
                if mensaje[x].lower() in ('l'):
                    print(mensaje[x])
                    lEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 1:
                if mensaje[x].lower() in ('i'):
                    print(mensaje[x])
                    lEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 2:
                if mensaje[x].lower() in ('s'):
                    print(mensaje[x])
                    lEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 3:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    lEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 4:
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    lEst = 4
                elif mensaje[x].lower() in ('a'):
                    print(mensaje[x])
                    lEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 5:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    lEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 6:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    lEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 7:
                if mensaje[x].lower() in ('r'):
                    print(mensaje[x])
                    lEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 8:
                if mensaje[x].lower() in ('i'):
                    print(mensaje[x])
                    lEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 9:
                if mensaje[x].lower() in ('b'):
                    print(mensaje[x])
                    lEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 10:
                if mensaje[x].lower() in ('u'):
                    print(mensaje[x])
                    lEst = 11
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 11:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    lEst = 12
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 12:
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    lEst = 13
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif lEst == 13:
                if mensaje[x].lower() in ('s'):
                    print(mensaje[x])
                    lEst = 14
                else:
                    print('Entrada invalida')
                    error = True
                    break
        if not error:
            print('sin error')


