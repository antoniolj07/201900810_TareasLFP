from select import Select
from maxi import Max
from mini import Min
from reporttokens import ReportTokens
from listattributes import ListAttributes
from count import Count
from suma import Suma
class ReportTo:
    def __init__(self, mensaje):
        self.afd_report_to(mensaje)
    
    def afd_report_to(self, mensaje):
        rEst = 0
        error = False
        archivohtml = ''
        comando = ''
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
                archivohtml = ''
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    rEst = 8
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('!','@','#','$','%','^','&','*','(',')','_'):
                    print(mensaje[x])
                    archivohtml = archivohtml + mensaje[x]
                    rEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 9:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('!','@','#','$','%','^','&','*','(',')','_'):
                    print(mensaje[x])
                    archivohtml = archivohtml + mensaje[x]
                    rEst = 9
                elif mensaje[x] in (' '):
                    print(mensaje[x])
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
                    print(mensaje[x])
                    rEst = 11
                elif mensaje[x].lower() in ('l'):
                    li = ListAttributes(comando)
                    break
                elif mensaje[x].lower() in ('m'):
                    print(mensaje[x])
                    rEst = 12
                elif mensaje[x].lower() in ('c'):
                    c = Count(comando)
                    break
                elif mensaje[x].lower() in ('r'):
                    r = ReportTokens(comando)
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 11:
                if mensaje[x].lower() in ('e'):
                    se = Select(comando)
                    break
                elif mensaje[x].lower() in ('u'):
                    su = Suma(comando)
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif rEst == 12:
                if mensaje[x].lower() in ('a'):
                    ma = Max(comando)
                    break
                elif mensaje[x].lower() in ('i'):
                    mi = Min(comando)
                    break
                else:
                    print('Entrada invalida')
                    error = True
                    break
            else:
                print('Entrada invalida')
                error = True
                break
        print(comando)
        print(archivohtml)