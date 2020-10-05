from reportto import ReportTo
from reporttokens import ReportTokens

class Report:
    def __init__(self, mensaje, nset={}):
        self.nset = nset
        self.afd_report(mensaje)
    
    def afd_report(self, mensaje):
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
                    rTokens = ReportTokens(mensaje, self.nset)
                    break
                elif mensaje[x] in (' '):
                    rTo = ReportTo(mensaje, self.nset)
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            else:
                print('Entrada invalida')
                error = True
                break