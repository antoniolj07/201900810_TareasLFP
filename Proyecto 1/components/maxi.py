class Max:
    def __init__(self, mensaje, nset):
        self.nset = nset
        self.afd_max(mensaje)

    def afd_max(self, mensaje):
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
                if mensaje[x].lower() in ('a'):
                    mEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif mEst == 2:
                if mensaje[x].lower() in ('x'):
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
            self.verMax(atributo)

    def verMax(self, atributo):
        maxAtri = -10000
        try:
            for registro in self.nset['archivos']:
                if not registro[atributo].lower() in ('null'):
                    if float(registro[atributo]) >= maxAtri:
                        maxAtri = float(registro[atributo])
            print('El valor maximo de {} es: {}'.format(atributo, maxAtri))
        except:
            print('Hubo error con el atributo: ',atributo)
            self.error = True
        self.atributo = atributo
        self.maxAtri = maxAtri
            

