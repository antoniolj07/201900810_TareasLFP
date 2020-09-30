class Min:
    def __init__(self, mensaje):
        self.afd_min(mensaje)

    def afd_min(self, mensaje):
        mEst = 0
        error = False
        atributo = ''
        for x in range(len(mensaje)):
            if mEst == 0:
                if mensaje[x].lower() in ('m'):
                    print(mensaje[x])
                    mEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 1:
                if mensaje[x].lower() in ('i'):
                    print(mensaje[x])
                    mEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 2:
                if mensaje[x].lower() in ('n'):
                    print(mensaje[x])
                    mEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 3:
                atributo = ''
                if mensaje[x].lower() in (' '):
                    print(mensaje[x])
                    mEst = 3
                elif mensaje[x].isalpha() or mensaje[x].isdigit():
                    print(mensaje[x])
                    atributo = atributo + mensaje[x]
                    mEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 4:
                if mensaje[x].isalpha() or mensaje[x].isdigit():
                    print(mensaje[x])
                    atributo = atributo + mensaje[x]
                    mEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
        
        if not error:
            print(atributo)
