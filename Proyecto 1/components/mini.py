class Min:
    def __init__(self, mensaje, nset):
        self.nset = nset
        self.afd_min(mensaje)

    def afd_min(self, mensaje):
        mEst = 0
        error = False
        atributo = ''
        for x in range(len(mensaje)):
            if mEst == 0:
                if mensaje[x].lower() in ('m'):
                    mEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 1:
                if mensaje[x].lower() in ('i'):
                    mEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 2:
                if mensaje[x].lower() in ('n'):
                    mEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 3:
                atributo = ''
                if mensaje[x].lower() in (' '):
                    mEst = 3
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    atributo = atributo + mensaje[x]
                    mEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 4:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    atributo = atributo + mensaje[x]
                    mEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
        self.error = error
        if not error:
            self.verMinimo(atributo)

    def verMinimo(self, atributo):
        minAtri = 1000000
        try:
            for registro in self.nset['archivos']:
                if not registro[atributo].lower() in ('null'):
                    if float(registro[atributo]) <= minAtri:
                        minAtri = float(registro[atributo])
            print('El valor maximo de {} es: {}'.format(atributo, minAtri))
        except:
            print('Hubo error con el atributo: ',atributo)
            self.error = True
        self.atributo = atributo
        self.minAtri = minAtri
