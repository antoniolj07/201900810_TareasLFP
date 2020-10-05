class UseSet:
    def __init__(self, mensaje):
        self.afd_use_set(mensaje)

    def afd_use_set(self, mensaje):
        uEst = 0
        setUsed = ''
        error = False
        for x in range(len(mensaje)):
            if uEst == 0:
                if mensaje[x].lower() in ('u'):
                    uEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif uEst == 1:
                if mensaje[x].lower() in ('s'):
                    uEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif uEst == 2:
                if mensaje[x].lower() in ('e'):
                    uEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif uEst == 3:
                if mensaje[x].lower() in (' '):
                    uEst = 3
                elif mensaje[x].lower() in ('s'):
                    uEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif uEst == 4:
                if mensaje[x].lower() in ('e'):
                    uEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif uEst == 5:
                setUsed = ''
                if mensaje[x].lower() in ('t'):
                    uEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif uEst == 6:
                if mensaje[x].lower() in (' '):
                    uEst = 6
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('-','_'):
                    setUsed = setUsed + mensaje[x]
                    uEst = 7
                else:
                    error = True
                    print('Entrada invalida shit')
                    break
            elif uEst == 7:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('-','_'):
                    setUsed = setUsed + mensaje[x]
                    uEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            else:
                print('Entrada invalida')
                break
        self.error = error
        if self.error:
            print('hubo error')
        else:
            self.uset = setUsed


