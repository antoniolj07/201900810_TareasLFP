from count import Count
class CreateSet:
    def __init__(self, mensaje):
        self.afd_create_set(mensaje)
            
    def afd_create_set(self, mensaje):
        entrada = ''
        cEst = 0
        newSet = {
            'idSet': '',
            'archivos': []
        }
        error = False
        for x in range(len(mensaje)):
            if cEst == 0:
                if mensaje[x].lower() in ('c'):
                    entrada = entrada + mensaje[x]
                    cEst = 1
                else:
                    error = True
                    print('Entrada incorrecta')
                    break
            elif cEst == 1:
                if mensaje[x].lower() in ('r'):
                    entrada = entrada + mensaje[x]
                    cEst = 2
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 2:
                if mensaje[x].lower() in ('e'):
                    entrada = entrada + mensaje[x]
                    cEst = 3
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 3:
                if mensaje[x].lower() in ('a'):
                    entrada = entrada + mensaje[x]
                    cEst = 4
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 4:
                if mensaje[x].lower() in ('t'):
                    entrada = entrada + mensaje[x]
                    cEst = 5
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 5:
                if mensaje[x].lower() in ('e'):
                    entrada = entrada + mensaje[x]
                    cEst = 6
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 6:
                if mensaje[x].lower() in (' '):
                    entrada = entrada + mensaje[x]
                    cEst = 6
                elif mensaje[x].lower() in ('s'):
                    entrada = entrada + mensaje[x]
                    cEst = 7
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 7:
                if mensaje[x].lower() in ('e'):
                    entrada = entrada + mensaje[x]
                    cEst = 8
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 8:
                if mensaje[x].lower() in ('t'):
                    newSet['idSet'] = ''
                    entrada = entrada + mensaje[x]
                    cEst = 9
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 9:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('-','_'):
                    newSet['idSet'] = newSet['idSet'] + mensaje[x]
                    entrada = entrada + mensaje[x]
                    cEst = 9
                elif mensaje[x] in (' '):
                    entrada = entrada + mensaje[x]
                    cEst = 9
                else:
                    error = True
                    print('Entrada invalida')
                    break
            elif cEst == 10:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('-','_'):
                    newSet['idSet'] = newSet['idSet'] + mensaje[x]
                    entrada = entrada + mensaje[x]
                    cEst = 10
                else:
                    error = True
                    print('Entrada invalida')
                    break
        self.error = error
        self.nSet = newSet