class ReportTokens:
    def __init__(self, mensaje):
        self.afd_report_tokens(mensaje)
    
    def afd_report_tokens(self, mensaje):
        rEst = 0
        error = False
        for x in range(len(mensaje)):
            if rEst == 0:
                if mensaje[x].lower() in ('r'):
                    print(mensaje[x])
                    rEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 1:
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    rEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 2:
                if mensaje[x].lower() in ('p'):
                    print(mensaje[x])
                    rEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 3:
                if mensaje[x].lower() in ('o'):
                    print(mensaje[x])
                    rEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 4:
                if mensaje[x].lower() in ('r'):
                    print(mensaje[x])
                    rEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 5:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    rEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 6:
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    rEst = 6
                elif mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    rEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 7:
                if mensaje[x].lower() in ('o'):
                    print(mensaje[x])
                    rEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 8:
                if mensaje[x].lower() in ('k'):
                    print(mensaje[x])
                    rEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 9:
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    rEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 10:
                if mensaje[x].lower() in ('n'):
                    print(mensaje[x])
                    rEst = 11
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 11:
                if mensaje[x].lower() in ('s'):
                    print(mensaje[x])
                    rEst = 12
                else:
                    print('Entrada invalida')
                    error = True
                    break
