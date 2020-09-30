class Count:
    countAtributes = []
    def __init__(self, mensaje):
        print('count')
        self.afd_count(mensaje)

    def afd_count(self, mensaje):
        entrada = ''
        cEst = 0
        newCountAtribute = ''
        for x in range(len(mensaje)):
            if cEst == 0:
                if mensaje[x].lower() in ('c'):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 1
                else:
                    print('Entrada invalida')
                    break
            elif cEst == 1:
                if mensaje[x].lower() in ('o'):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 2
                else:
                    print('Entrada invalida')
                    break
            elif cEst == 2:
                if mensaje[x].lower() in ('u'):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 3
                else:
                    print('Entrada invalida')
                    break
            elif cEst == 3:
                if mensaje[x].lower() in ('n'):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 4
                else:
                    print('Entrada invalida')
                    break
            elif cEst == 4:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 5
                else:
                    print('Entrada invalida')
                    break
            elif cEst == 5:
                newCountAtribute = ''
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 5
                elif mensaje[x] in ('*'):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    cEst = 6
                elif mensaje[x].isalpha():
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    newCountAtribute = newCountAtribute + mensaje[x]
                    if x == len(mensaje) - 1:
                        self.countAtributes.append(newCountAtribute)
                    cEst = 7
                else:
                    print('Entrada invalida')
                    break
            elif cEst == 6:
                print('*')
            elif cEst == 7:
                if mensaje[x].isalpha():
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    newCountAtribute = newCountAtribute + mensaje[x]
                    if x == len(mensaje) - 1:
                        self.countAtributes.append(newCountAtribute)
                    cEst = 7
                elif mensaje[x] in (','):
                    print(mensaje[x])
                    entrada = entrada + mensaje[x]
                    self.countAtributes.append(newCountAtribute)
                    cEst = 5
                else:
                    print('Entrada invalida, fuck')
                    break
        print(self.countAtributes)
            