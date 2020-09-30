class Select:
    def __init__(self, mensaje):
        print('select')
        self.afd_select(mensaje)
    
    def afd_select(self, mensaje):
        atributos = []
        condiciones = []
        sEst = 0
        error = False
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
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    sEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 2:
                if mensaje[x].lower() in ('l'):
                    print(mensaje[x])
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 3:
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    sEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 4:
                if mensaje[x].lower() in ('c'):
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
                nAtri = ''
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 6
                elif mensaje[x] in ('*'):
                    print(mensaje[x])
                    nAtri = '*'
                    atributos.append(nAtri)
                    sEst = 8
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    print(mensaje[x])
                    nAtri = nAtri + mensaje[x]
                    sEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 7:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    print(mensaje[x])
                    nAtri = nAtri + mensaje[x]
                    sEst = 7
                elif mensaje[x] in (','):
                    print(mensaje[x])
                    atributos.append(nAtri)
                    sEst = 6
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    atributos.append(nAtri)
                    sEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 8:
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 8
                elif mensaje[x].lower() in ('w'):
                    print(mensaje[x])
                    sEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 9:
                if mensaje[x].lower() in ('h'):
                    print(mensaje[x])
                    sEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 10:
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    sEst = 11
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 11:
                if mensaje[x].lower() in ('r'):
                    print(mensaje[x])
                    sEst = 12
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 12:
                if mensaje[x].lower() in ('e'):
                    print(mensaje[x])
                    sEst = 13
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 13:
                nCondi = {
                    'atributo': '',
                    'valor': '',
                    'signo': '',
                    'tipo': ''
                }
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 13
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    print(mensaje[x])
                    nCondi['atributo'] = nCondi['atributo'] + mensaje[x]
                    sEst = 14
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 14:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    print(mensaje[x])
                    nCondi['atributo'] = nCondi['atributo'] + mensaje[x]
                    sEst = 14
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 14
                elif mensaje[x] in ('='):
                    print(mensaje[x])
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 15
                elif mensaje[x] in ('<','>'):
                    print(mensaje[x])
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 23
                elif mensaje[x] in ('!'):
                    print(mensaje[x])
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 24
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 23:
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 15
                elif mensaje[x] in ('='):
                    print(mensaje[x])
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 15
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 24:
                if mensaje[x] in ('='):
                    print(mensaje[x])
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 15
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 15:
                if mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 15
                elif mensaje[x] in ('\"'):
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    nCondi['tipo'] = 'string'
                    sEst = 16
                elif mensaje[x].isdigit():
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    nCondi['tipo'] = 'number'
                    if x == len(mensaje) - 1:
                        condiciones.append(nCondi)
                    sEst = 17
                elif mensaje[x].isalpha():
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    nCondi['tipo'] = 'boolean'
                    sEst = 18
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 16:
                if not mensaje[x] in ('\"'):
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    sEst == 16
                elif mensaje[x] in ('\"'):
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    condiciones.append(nCondi)
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 17:
                if (mensaje[x].isdigit() or mensaje[x] in ('.')):
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    if x == len(mensaje) - 1:
                        condiciones.append(nCondi)
                    sEst = 17
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    condiciones.append(nCondi)
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 18:
                if mensaje[x].lower() in ('t','r','u','e','f','a','l','s'):
                    print(mensaje[x])
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    if x == len(mensaje) - 1:
                        condiciones.append(nCondi)
                    sEst = 18
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    condiciones.append(nCondi)
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 19:
                if mensaje[x].lower() in ('a'):
                    print(mensaje[x])
                    sEst = 20
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 20:
                if mensaje[x].lower() in ('n'):
                    print(mensaje[x])
                    sEst = 21
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 20
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 21:
                if mensaje[x].lower() in ('d'):
                    print(mensaje[x])
                    sEst = 22
                elif mensaje[x] in (' '):
                    print(mensaje[x])
                    sEst = 21
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 22:
                if mensaje[x].lower() in (' '):
                    print(mensaje[x])
                    sEst = 13
                else:
                    print('Entrada invalida')
                    error = True
                    break
            else:
                print('Entrada invalida')
                error = True
                break
        
        if error:
            print('hubo error')
        else:
            print(atributos)
            print(condiciones)


                
            