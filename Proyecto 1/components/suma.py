class Suma:
    def __init__(self, mensaje, nset):
        self.nset = nset
        self.afd_suma(mensaje)

    def afd_suma(self, mensaje):
        sEst = 0
        error = False
        atributos = []
        for x in range(len(mensaje)):
            if sEst == 0:
                if mensaje[x].lower() in ('s'):
                    sEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 1:
                if mensaje[x].lower() in ('u'):
                    sEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 2:
                if mensaje[x].lower() in ('m'):
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 3:
                nAtri = ''
                if mensaje[x] in (' '):
                    sEst = 3
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    nAtri = nAtri + mensaje[x]
                    if x == len(mensaje) - 1:
                        atributos.append(nAtri)
                    sEst = 4
                elif mensaje[x] in ('*'):
                    nAtri = nAtri + mensaje[x]
                    atributos.append(nAtri)
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 4:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    nAtri = nAtri + mensaje[x]
                    if x == len(mensaje) - 1:
                        atributos.append(nAtri)
                    sEst = 4
                elif mensaje[x] in (','):
                    atributos.append(nAtri)
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
        self.error = error
        if not error:
            self.verSuma(atributos)

    def verSuma(self, atributos):
        sumas = {}
        if not ('*') in atributos:
            for atributo in atributos:
                sumas[atributo] = 0

            for registro in self.nset['archivos']:
                for atributo in atributos:
                    try:
                        sumas[atributo] = sumas[atributo] + float(registro[atributo])
                    except:
                        sumas[atributo] = sumas[atributo]
            for a in atributos:
                print('La suma de {} es: {}'.format(a, sumas[a]))
        else:
            keys = []
            for key in self.nset['archivos'][0].keys():
                sumas[key] = 0
                keys.append(key)
            
            for registro in self.nset['archivos']:
                for atributo in keys:
                    try:
                        sumas[atributo] = sumas[atributo] + float(registro[atributo])
                    except:
                        sumas[atributo] = sumas[atributo]
            for atributo in keys:
                print('La suma de {} es: {}'.format(atributo, sumas[atributo]))

        self.sumas = sumas
        
