class Script:
    def __init__(self, mensaje):
        self.afd_script(mensaje)
    
    def afd_script(self, mensaje):
        sEst = 0
        error = False
        paths = []
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
                if mensaje[x].lower() in ('c'):
                    print(mensaje[x])
                    sEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 2:
                if mensaje[x].lower() in ('r'):
                    print(mensaje[x])
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 3:
                if mensaje[x].lower() in ('i'):
                    print(mensaje[x])
                    sEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 4:
                if mensaje[x].lower() in ('p'):
                    print(mensaje[x])
                    sEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 5:
                if mensaje[x].lower() in ('t'):
                    print(mensaje[x])
                    sEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 6:
                path = ''
                if mensaje[x].lower() in (' '):
                    print(mensaje[x])
                    sEst = 6
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('/',':','.'):
                    print(mensaje[x])
                    path = path + mensaje[x]
                    if x == len(mensaje) - 1:
                        paths.append(path)
                    sEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 7:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('/',':','.'):
                    print(mensaje[x])
                    path = path + mensaje[x]
                    if x == len(mensaje) - 1:
                        paths.append(path)
                    sEst = 7
                elif mensaje[x] in (','):
                    print(mensaje[x])
                    paths.append(path)
                    sEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
        if not error:
            print(paths)
