class Suma:
    def __init__(self, mensaje):
        self.afd_suma(mensaje)

    def afd_suma(self, mensaje):
        sEst = 0
        error = False
        atributos = []
        for x in range(len(mensaje)):
            if sEst == 0:
                if mensaje[x].lower() in ('s'):
                    print(mensaje[x])
                    sEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 1:
                if mensaje[x].lower() in ('u'):
                    print(mensaje[x])
                    sEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 2:
                if mensaje[x].lower() in ('m'):
                    print(mensaje[x])
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 3:
                nAtri = ''
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 3
                elif mensaje[x].isalpha():
                    print(mensaje[x])
                    nAtri = nAtri + mensaje[x]
                    if x == len(mensaje) - 1:
                        atributos.append(nAtri)
                    sEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 4:
                if mensaje[x].isalpha():
                    print(mensaje[x])
                    nAtri = nAtri + mensaje[x]
                    if x == len(mensaje) - 1:
                        atributos.append(nAtri)
                    sEst = 4
                elif mensaje[x] in (','):
                    print(mensaje[x])
                    atributos.append(nAtri)
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
        if not error:
            print(atributos)
