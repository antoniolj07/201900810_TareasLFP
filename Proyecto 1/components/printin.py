class PrintIn:
    def __init__(self, mensaje):
        self.aft_print_in(mensaje)

    def aft_print_in(self, mensaje):
        pEst = 0
        error = False
        color = ''
        for x in range(len(mensaje)):
            if pEst == 0:
                if mensaje[x].lower() in ('p'):
                    print(mensaje[x])
                    pEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 1:
                if mensaje[x].lower() in ('r'):
                    print(mensaje[x])
                    pEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 2:
                if mensaje[x].lower() in ('i'):
                    print(mensaje[x])
                    pEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 3:
                if mensaje[x].lower() in ('n'):
                    print(mensaje[x])
                    pEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 4:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    pEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 5:
                if mensaje[x].lower() in (' '):
                    print(mensaje[x])
                    pEst = 5
                elif mensaje[x].lower() in ('i'):
                    print(mensaje[x])
                    pEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 6:
                if mensaje[x].lower() in ('n'):
                    print(mensaje[x])
                    pEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 7:
                color = ''
                if mensaje[x].lower() in (' '):
                    print(mensaje[x])
                    pEst = 7
                elif mensaje[x].isalpha():
                    color = color + mensaje[x]
                    print(mensaje[x])
                    pEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 8:
                if mensaje[x].isalpha():
                    print(mensaje[x])
                    color = color + mensaje[x]
                    pEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
        print(color)
