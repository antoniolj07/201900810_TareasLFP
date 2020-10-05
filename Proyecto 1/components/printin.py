class PrintIn:
    def __init__(self, mensaje):
        self.aft_print_in(mensaje)

    def aft_print_in(self, mensaje):
        pEst = 0
        error = False
        color = ''
        for x in range(len(mensaje)):
            if pEst == 0:
                if mensaje[x].lower() in ('p'):
                    pEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 1:
                if mensaje[x].lower() in ('r'):
                    pEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 2:
                if mensaje[x].lower() in ('i'):
                    pEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 3:
                if mensaje[x].lower() in ('n'):
                    pEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 4:
                if mensaje[x].lower() in ('t'):
                    pEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 5:
                if mensaje[x].lower() in (' '):
                    pEst = 5
                elif mensaje[x].lower() in ('i'):
                    pEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 6:
                if mensaje[x].lower() in ('n'):
                    pEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 7:
                color = ''
                if mensaje[x].lower() in (' '):
                    pEst = 7
                elif mensaje[x].isalpha():
                    color = color + mensaje[x]
                    pEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif pEst == 8:
                if mensaje[x].isalpha():
                    color = color + mensaje[x]
                    pEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
        if not error:
            self.color = color
            self.verColor()

    def verColor(self):
        if self.color.lower() in ('blue'):
            self.codigo= '\033[1;34;40m';
            print(self.codigo + 'Imprimiendo en BLUE')
        elif self.color.lower() in ('red'):
            self.codigo= '\033[1;31;40m';
            print(self.codigo + 'Imprimiendo en RED')
        elif self.color.lower() in ('green'):
            self.codigo = '\033[1;32;40m'
            print(self.codigo + 'Imprimiendo en GREEN')
        elif self.color.lower() in ('yellow'):
            self.codigo= '\033[1;33;40m';
            print(self.codigo + 'Imprimiendo en YELLOW')
        elif self.color.lower() in ('orange'):
            self.codigo= '\033[1;39;40m';
            print(self.codigo + 'Imprimiendo en ORANGE')
        elif self.color.lower() in ('pink'):
            self.codigo= '\033[1;35;40m';
            print(self.codigo + 'Imprimiendo en PINK')
        else:
            print('No se reconoce el color')