class Count:
    countAtributes = []
    def __init__(self, mensaje, nset):
        self.cuentas = {}
        self.nset = nset
        self.afd_count(mensaje)

    def afd_count(self, mensaje):
        entrada = ''
        cEst = 0
        newCountAtribute = ''
        error = False
        for x in range(len(mensaje)):
            if cEst == 0:
                if mensaje[x].lower() in ('c'):
                    cEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif cEst == 1:
                if mensaje[x].lower() in ('o'):
                    cEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif cEst == 2:
                if mensaje[x].lower() in ('u'):
                    cEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif cEst == 3:
                if mensaje[x].lower() in ('n'):
                    cEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif cEst == 4:
                if mensaje[x].lower() in ('t'):
                    cEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif cEst == 5:
                newCountAtribute = ''
                if mensaje[x] in (' '):
                    cEst = 5
                elif mensaje[x] in ('*'):
                    newCountAtribute = newCountAtribute + mensaje[x]
                    self.countAtributes.append(newCountAtribute)
                    cEst = 6
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    newCountAtribute = newCountAtribute + mensaje[x]
                    if x == len(mensaje) - 1:
                        self.countAtributes.append(newCountAtribute)
                    cEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif cEst == 6:
                print()
            elif cEst == 7:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    newCountAtribute = newCountAtribute + mensaje[x]
                    if x == len(mensaje) - 1:
                        self.countAtributes.append(newCountAtribute)
                    cEst = 7
                elif mensaje[x] in (','):
                    self.countAtributes.append(newCountAtribute)
                    cEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
        self.error = error
        if not error:
            self.verCueta()

    def verCueta(self):
        self.cuentas = {}
        if not ('*') in self.countAtributes:
            for atri in self.countAtributes:
                self.cuentas[atri] = 0
            
            for registro in self.nset['archivos']:
                for atributo in self.countAtributes:
                    if not registro[atributo].lower() in ('null'):
                        self.cuentas[atributo] = self.cuentas[atributo] + 1
        else:
            keys = []
            for atributo in self.nset['archivos'][0].keys():
                self.cuentas[atributo] = 0
                keys.append(atributo)
            print(keys)
            for registro in self.nset['archivos']:
                for atributo in keys:
                    if not registro[atributo].lower() in ('null'):
                        self.cuentas[atributo] = self.cuentas[atributo] + 1
        print(self.cuentas)