from comandolet import ComandoLet

class JsAfd:
    def __init__(self):
        self.leerRuta()

    def leerRuta(self):
        print('Ingrese la ruta del Script que desea ver')
        ruta = input()
        contenido = []
        try:
            with open( ruta, 'r') as f:
                lineas = f.readlines()
                i = 1
                for linea in lineas:
                    lcontenido = ''
                    for x in range(len(linea)):
                        if not linea[x] in ('\n'):
                            lcontenido = lcontenido + linea[x]
                        else:
                            lcontenido = lcontenido + ' '
                        
                    neolinea = {
                        'contenido': lcontenido,
                        'linea': i
                    }
                    contenido.append(neolinea)
                    i = i + 1
        except:
            print('No se pudo leer el archivo')
        self.afd(contenido)

    def afd(self, contenido):
        tokensTotales = []
        errores = []
        e = 0
        dest = 0
        lest = 0
        vest= 0
        cest = 0 
        iest = 0 
        west = 0 
        sest = 0
        fest = 0
        yest = 0

        scest = 0
        sdest = 0
        sbest = 0
        tok = {
            'lexema': '',
            'token': '',
            'descripcion': '',
            'linea': '',
            'columna': ''
        }
        for linea in contenido:
            for x in range(len(linea['contenido'])):
                if e == 0:
                    if linea['contenido'][x] in ('/'):
                        print(linea['contenido'][x])
                        e = 1
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('l'):
                        print(linea['contenido'][x])
                        e = 2
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('v'):
                        print(linea['contenido'][x])
                        e = 3
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('c'):
                        print(linea['contenido'][x])
                        e = 4
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('i'):
                        print(linea['contenido'][x])
                        e = 5
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('w'):
                        print(linea['contenido'][x])
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                        e = 6
                    elif linea['contenido'][x] in ('f'):
                        print(linea['contenido'][x])
                        e = 7
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('s'):
                        print(linea['contenido'][x])
                        e = 8
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('d'):
                        print(linea['contenido'][x])
                        e = 9
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('b'):
                        print(linea['contenido'][x])
                        e = 13
                        tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        tok['linea'] = linea['linea']
                        tok['columna'] = x + 1
                    elif linea['contenido'][x] in ('}'):
                        print(linea['contenido'][x])
                        e = 0
                        tok = {'lexema': '}', 'token': 'tkn_llave_cerrada', 'descripcion': 'llave cerrada',
                        'linea': linea['linea'], 'columna': x + 1}
                        tokensTotales.append(tok)
                        tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                    elif linea['contenido'][x] in (' '):
                        e = 0
                    else:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            e = 10
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                        elif linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                        elif linea['contenido'][x] in (chr(9)):
                            print(linea['contenido'][x])
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error :(')
                            e = 0
                elif e == 1:
                    if dest == 0:
                        if linea['contenido'][x] in ('*'): 
                            print(linea['contenido'][x])
                            dest = 1
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_diagonal_asterisco'
                            tok['descripcion'] = 'inicio de comentario'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                        else:
                            print('Error en linea {} columna {}'.format(linea['linea'], x))
                            error = {'linea': linea['linea'], 'columna': x}
                            errores.append(error)
                    elif dest == 1:
                        if not linea['contenido'][x] in ('*'):
                            print(linea['contenido'][x])
                            dest = 1
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_contenido_comentario'
                            tok['descripcion'] = 'cuerpo del comentario'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                        elif linea['contenido'][x] in ('*'):
                            print(linea['contenido'][x])
                            dest = 2
                    elif dest == 2:
                        if linea['contenido'][x] in ('/'):
                            tokensTotales.append(tok)
                            tok = {'lexema': '*/', 'token': 'tkn_asterisco_diagonal', 'descripcion': 'cierre de comentario',
                            'linea': linea['linea'], 'columna': x+1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            print(linea['contenido'][x])
                            dest = 0
                            e = 0
                        else:
                            tok['lexema'] = tok['lexema'] + '*' + linea['contenido'][x]
                            print(linea['contenido'][x])
                            dest = 1
                elif e == 2:
                    if lest == 0:
                        if linea['contenido'][x] in ('e'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            lest = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            lest = 0
                            e = 10
                    elif lest == 1:
                        if linea['contenido'][x] in ('t'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            lest = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            lest = 0
                            e = 10
                    elif lest == 2:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_let'
                            tok['descripcion'] = 'palabra reservada let'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            lest = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            lest = 0
                            e = 10
                            print('no hay un espacio')
                    elif lest == 3:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'nombre del identificador'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            lest = 4
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif lest == 4:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_') or linea['contenido'][x].isdigit():
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            lest = 4
                        elif linea['contenido'][x] in (' '):
                            lest = 4
                        elif linea['contenido'][x] in ('='):
                            tokensTotales.append(tok)
                            tok = {'lexema': '=', 'token': 'tkn_igual', 'descripcion': 'signo igual', 'linea': linea['linea'],
                            'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            lest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif lest == 5:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            lest = 5
                        elif linea['contenido'][x].isalpha():
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_boolean'
                            tok['descripcion'] = 'palabra reservada booleana'
                            lest = 7
                        elif linea['contenido'][x].isdigit() or linea['contenido'][x] in ('-','+'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_numero'
                            tok['descripcion'] = 'numero'
                            lest = 7
                        elif linea['contenido'][x] in ('\"'):
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            lest = 6
                        elif linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            e = 11
                            lest = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif lest == 6:
                        if not linea['contenido'][x] in ('\"'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['descripcion'] = 'cadena de texto'
                            tok['token'] = 'tkn_cadena_texto'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            lest = 6
                        elif linea['contenido'][x] in ('\"'):
                            tokensTotales.append(tok)
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            lest = 8
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif lest == 7:
                        if linea['contenido'][x].isalpha():
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_boolean'
                            tok['descripcion'] = 'palabra reservada booleano'
                            lest = 7
                        elif linea['contenido'][x].isdigit() or linea['contenido'][x] in ('.'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_numero'
                            tok['descripcion'] = 'numero'
                            lest = 7
                        elif linea['contenido'][x] in (';'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            lest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif lest == 8:
                        if linea['contenido'][x] in (';'):
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma', 'linea': linea['linea'],
                            'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            lest = 0
                            e = 0
                        elif linea['contenido'][x] in (' '):
                            lest = 8
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 3:
                    if vest == 0:
                        if linea['contenido'][x] in ('a'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            vest = 1
                        else:
                            e = 10
                            vest = 0
                    elif vest == 1:
                        if linea['contenido'][x] in ('r'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            vest = 2
                        else:
                            e = 10
                            vest = 0
                    elif vest == 2:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_var'
                            tok['descripcion'] = 'palabra reservada var'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            vest = 3
                        else:
                            e = 10
                            vest = 0
                    elif vest == 3:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'nombre del identificador'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            vest = 4
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif vest == 4:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            print(linea['contenido'][x])
                            vest = 4
                        elif linea['contenido'][x] in (' '):
                            vest = 4
                        elif linea['contenido'][x] in ('='):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': '=', 'token': 'tkn_signo_igual', 'descripcion': 'signo igual',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            vest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif vest == 5:
                        if linea['contenido'][x] in ('\"'):
                            print(linea['contenido'][x])
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles abiertas',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            vest = 6
                        elif linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            e = 11
                            vest = 0
                        elif linea['contenido'][x].isalpha():
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            vest = 8
                        elif linea['contenido'][x].isdigit() or linea['contenido'][x] in ('-','+'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_numero'
                            tok['descripcion'] = 'numero'
                            vest = 8
                        elif linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            vest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif vest == 6:
                        if not linea['contenido'][x] in ('\"'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_cadena_texto'
                            tok['descripcion'] = 'cadena de texto'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            vest = 6
                        elif linea['contenido'][x] in ('\"'):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles cerradas',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            vest = 7
                    elif vest == 7:
                        if linea['contenido'][x] in (';'):
                            print(linea['contenido'][x])
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma', 'linea': linea['linea'],
                            'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            vest = 0
                            e = 0
                        elif linea['contenido'][x] in (' '):
                            vest = 7
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif vest == 8:
                        if linea['contenido'][x].isalpha():
                            tok['token'] = 'tkn_boolean'
                            tok['descripcion'] = 'palabra reservada booleana'
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            vest = 8
                        elif linea['contenido'][x].isdigit() or linea['contenido'][x] in ('.'):
                            tok['token'] = 'tkn_numero'
                            tok['descripcion'] = 'asignacion de numero'
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            vest = 8
                        elif linea['contenido'][x] in (' '):
                            vest = 8
                        elif linea['contenido'][x] in (';'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            vest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 4:
                    if cest == 0:
                        if linea['contenido'][x] in ('o'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            cest = 1
                        elif linea['contenido'][x] in ('a'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            e = 12
                            cest = 0
                        else:
                            cest = 0
                            e = 10
                    elif cest == 1:
                        if linea['contenido'][x] in ('n'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            cest = 2
                        else:
                            cest = 0
                            e = 10
                    elif cest == 2:
                        if linea['contenido'][x] in ('s'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            cest = 3
                        else:
                            cest = 0
                            e = 10
                    elif cest == 3:
                        if linea['contenido'][x] in ('t'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            cest = 4
                        else:
                            cest = 0
                            e = 10
                    elif cest == 4:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_const'
                            tok['descripcion'] = 'palabra reservada const'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 5
                        else:
                            cest = 0
                            e = 10
                    elif cest == 5:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'nombre del identificador'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            cest = 6
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif cest == 6:
                        if linea['contenido'][x].isdigit() or linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            cest = 6
                        elif linea['contenido'][x] in (' '):
                            cest = 6
                        elif linea['contenido'][x] in ('='):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': '=', 'token': 'tkn_signo_igual', 'descripcion': 'signo igual',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 7
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif cest == 7:
                        if linea['contenido'][x] in (' '):
                            cest = 7
                        elif linea['contenido'][x].isdigit() or linea['contenido'][x] in ('-','+','.'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_numero'
                            tok['descripcion'] = 'numero'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            cest = 7
                        elif linea['contenido'][x].isalpha():
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_bool'
                            tok['descripcion'] = 'boleano'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            cest = 8
                        elif linea['contenido'][x] in ('\"'):
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 9
                        elif linea['contenido'][x] in ('('):
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 0
                            e = 11
                        elif linea['contenido'][x] in (';'):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif cest == 8:
                        if linea['contenido'][x].isalpha():
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            cest = 8
                        elif linea['contenido'][x] in (' '):
                            cest = 8
                        elif linea['contenido'][x] in (';'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif cest == 9:
                        if not linea['contenido'][x] in ('\"'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_cadena_texto'
                            tok['descripcion'] = 'cadena de texto'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            cest = 9
                        elif linea['contenido'][x] in ('\"'):
                            tokensTotales.append(tok)
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 10
                    elif cest == 10:
                        if linea['contenido'][x] in (';'):
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            cest = 0
                            e = 0
                        elif linea['contenido'][x] in (' '):
                            cest = 10
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 5:
                    if iest == 0:
                        if linea['contenido'][x] in ('f'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            iest = 1
                        else:
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            iest = 0
                            e = 10
                    elif iest == 1:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_if'
                            tok['descripcion'] = 'palabra reservada if'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            iest = 2
                        elif linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_if'
                            tok['descripcion'] = 'palabra reservada if'
                            tokensTotales.append(tok)
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            iest = 3
                        else:
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            iest = 0
                            e = 10
                    elif iest == 2:
                        if linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            iest = 3
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif iest == 3:
                        if linea['contenido'][x].isalpha():
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            if not linea['contenido'][x] in ('t','f'):
                                tok['token'] = 'tkn_identificador'
                                tok['descripcion'] = 'identificador en un if'
                                iest = 4
                            else:
                                iest = 5
                        elif linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador en un if'
                            iest = 4
                        elif linea['contenido'][x] in (' '):
                            iest = 3
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif iest == 4:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_') or linea['contenido'][x].isdigit():
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        elif linea['contenido'][x] in (')'):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            iest = 6
                        elif linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            iest = 4
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif iest == 5:
                        if linea['contenido'][x].isalpha():
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            if linea['contenido'][x] in ('r','u','e','a','l','s'):
                                if linea['contenido'][x] in ('r'):
                                    tok['token'] = 'tkn_true'
                                    tok['descripcion'] = 'palabra reservada true'
                                elif linea['contenido'][x] in ('a'):
                                    tok['token'] = 'tkn_false'
                                    tok['descripcion'] = 'palabra reservada false'
                                iest = 5
                            else:
                                iest = 4
                        elif linea['contenido'][x] in ('_') or linea['contenido'][x].isdigit():
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador en un if'
                            iest = 4
                        elif linea['contenido'][x] in (')'):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            iest = 6
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif iest == 6:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            iest = 6
                        elif linea['contenido'][x] in ('{'):
                            print(linea['contenido'][x])
                            tok = {'lexema': '{', 'token': 'tkn_llave_abierta', 'descripcion': 'llave abierta',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            iest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 6:
                    if west == 0:
                        if linea['contenido'][x] in ('h'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 0
                            e = 10
                    elif west == 1:
                        if linea['contenido'][x] in ('i'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 0
                            e = 10
                    elif west == 2:
                        if linea['contenido'][x] in ('l'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 0
                            e = 10
                    elif west == 3:
                        if linea['contenido'][x] in ('e'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 4
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 0
                            e = 10
                    elif west == 4:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_while'
                            tok['descripcion'] = 'palabra reservada while'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            west = 5
                        elif linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_while'
                            tok['descripcion'] = 'palabra reservada while'
                            tokensTotales.append(tok)
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            west = 6
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            west = 0
                            e = 10
                    elif west == 5:
                        if linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            west = 6
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif west == 6:
                        if linea['contenido'][x].isalpha():
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            if not linea['contenido'][x] in ('t','f'):
                                tok['token'] = 'tkn_identificador'
                                tok['descripcion'] = 'identificador en un while'
                                west = 7
                            else:
                                west = 8
                        elif linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador en un while'
                            west = 7
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif west == 7:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                        elif linea['contenido'][x] in (')'):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            west = 9
                        elif linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            west = 7
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif west == 8:
                        if linea['contenido'][x].isalpha():
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            if linea['contenido'][x] in ('r','u','e','a','l','s'):
                                if linea['contenido'][x] in ('r'):
                                    tok['token'] = 'tkn_true'
                                    tok['descripcion'] = 'palabra reservada true'
                                elif linea['contenido'][x] in ('a'):
                                    tok['token'] = 'tkn_false'
                                    tok['descripcion'] = 'palabra reservada false'
                                west = 8
                            else:
                                west = 7
                        elif linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador en un if'
                            west = 7
                        elif linea['contenido'][x] in (')'):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            west = 9
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif west == 9:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            west = 9
                        elif linea['contenido'][x] in ('{'):
                            print(linea['contenido'][x])
                            tok = {'lexema': '{', 'token': 'tkn_llave_abierta', 'descripcion': 'llave abierta',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            west = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                        
                elif e == 7:
                    if fest == 0:
                        if linea['contenido'][x] in ('o'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 1:
                        if linea['contenido'][x] in ('r'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 2:
                        if linea['contenido'][x] in ('e'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 3:
                        if linea['contenido'][x] in ('a'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 4
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 4:
                        if linea['contenido'][x] in ('c'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 5
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 5:
                        if linea['contenido'][x] in ('h'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 6
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 6:
                        if linea['contenido'][x] in (' '):
                            tok['token'] = 'tkn_foreach'
                            tok['descripcion'] = 'palabra reservada foreach'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 7
                        elif linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok['token'] = 'tkn_foreach'
                            tok['descripcion'] = 'palabra reservada foreach'
                            tokensTotales.append(tok)
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 8
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 0
                            e = 10
                    elif fest == 7:
                        if linea['contenido'][x] in ('('):
                            print(linea['contenido'][x])
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 8
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 8:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_elemento_identificador'
                            tok['descripcion'] = 'elemendo de un arreglo en un foreach'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            fest = 9
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 9:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 9
                        elif linea['contenido'][x] in (' '):
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 10
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 10:
                        if linea['contenido'][x] in ('i'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            fest = 11
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 11:
                        if linea['contenido'][x] in ('n'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 12
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 12:
                        if linea['contenido'][x] in (' '):
                            tok['token'] = 'tkn_in'
                            tok['descripcion'] = 'palabra reservada in'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 13
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 13:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] = linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            fest = 14
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 14:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 14
                        elif linea['contenido'][x] in (')'):
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'coleccion de elementos para foreach'
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 15
                        elif linea['contenido'][x] in (' '):
                            fest = 14
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 15:
                        if linea['contenido'][x] in (' '):
                            fest = 15
                        elif linea['contenido'][x] in ('{'):
                            tok = {'lexema': '{', 'token': 'tkn_llave_abierta', 'descripcion': 'llave abierta',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 8:
                    if sest == 0:
                        if linea['contenido'][x] in ('w'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 0
                            e = 10
                    elif sest == 1:
                        if linea['contenido'][x] in ('i'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 0
                            e = 10
                    elif sest == 2:
                        if linea['contenido'][x] in ('t'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 0
                            e = 10
                    elif sest == 3:
                        if linea['contenido'][x] in ('c'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 4
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 0
                            e = 10
                    elif sest == 4:
                        if linea['contenido'][x] in ('h'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 5
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 0
                            e = 10
                    elif sest == 5:
                        if linea['contenido'][x] in (' '):
                            tok['token'] = 'tkn_switch'
                            tok['descripcion'] = 'palabra reservada switch'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sest = 6
                        elif linea['contenido'][x] in ('('):
                            tok['token'] = 'tkn_switch'
                            tok['descripcion'] = 'palabra reservada switch'
                            tokensTotales.append(tok)
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abiertos',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sest = 7
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 0
                            e = 10
                    elif sest == 6:
                        if linea['contenido'][x] in ('('):
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abiertos',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sest = 7
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif sest == 7:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador del switch'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            sest = 8
                        elif linea['contenido'][x] in (' '):
                            sest = 7
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif sest == 8:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sest = 8
                        elif linea['contenido'][x] in (')'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sest = 9
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif sest == 9:
                        if linea['contenido'][x] in (' '):
                            sest = 9
                        elif linea['contenido'][x] in ('{'):
                            tok = {'lexema': '{', 'token': 'tkn_llave_abierta', 'descripcion': 'llave abierta',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sest = 0
                            e = 0
                elif e == 9:
                    if sdest == 0:
                        if linea['contenido'][x] in ('e'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                    elif sdest == 1:
                        if linea['contenido'][x] in ('f'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                    elif sdest == 2:
                        if linea['contenido'][x] in ('a'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                    elif sdest == 3:
                        if linea['contenido'][x] in ('u'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 4
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                    elif sdest == 4:
                        if linea['contenido'][x] in ('l'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 5
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                    elif sdest == 5:
                        if linea['contenido'][x] in ('t'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 6
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                    elif sdest == 6:
                        if linea['contenido'][x] in (' '):
                            sdest = 6
                        elif linea['contenido'][x] in (':'):
                            tok['token'] = 'tkn_default'
                            tok['descripcion'] = 'palabra reservada default'
                            tokensTotales.append(tok)
                            tok = {'lexema': ':', 'token': 'tkn_dos_puntos', 'descripcion': 'dos puntos para default',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sdest = 0
                            e = 0
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sdest = 0
                            e = 10
                elif e == 10:
                    if yest == 0:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            yest = 0
                        elif linea['contenido'][x] in ('('):
                            tok['token'] = 'tkn_identificador_funcion'
                            tok['descripcion'] = 'llamada a funcion'
                            tokensTotales.append(tok)
                            tok = {'lexema': '(', 'token': 'tkn_parentesis_abierto', 'descripcion': 'parentesis abierto',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 1
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif yest == 1:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador en parametro en llamada de funcion'
                            yest = 2
                        elif linea['contenido'][x].isdigit() or linea['contenido'][x] in ('-','+'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_numero'
                            tok['descripcion'] = 'numero en llamada de funcion'
                            yest = 6
                        elif linea['contenido'][x] in ('\"'):
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles en llamada funcion',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': linea['linea'], 'columna': x + 1}
                            yest = 3
                        elif linea['contenido'][x] in (' '):
                            yest = 1
                        elif linea['contenido'][x] in (')'):
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': linea['linea'], 'columna': x + 1}
                            yest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif yest == 2:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            yest = 2
                        elif linea['contenido'][x] in (','):
                            tokensTotales.append(tok)
                            tok = {'lexema': ',', 'token': 'tkn_coma', 'descripcion': 'coma entre parametros',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 1
                        elif linea['contenido'][x] in (' '):
                            yest = 2
                        elif linea['contenido'][x] in (')'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif yest == 3:
                        if not linea['contenido'][x] in ('\"'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_cadena_texto'
                            tok['descripcion'] = 'cadena de texto como parametro de funcion'
                            yest = 3
                        elif linea['contenido'][x] in ('\"'):
                            tokensTotales.append(tok)
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 4
                    elif yest == 4:
                        if linea['contenido'][x] in (' '):
                            yest = 4
                        elif linea['contenido'][x] in (','):
                            tok = {'lexema': ',', 'token': 'tkn_coma', 'descripcion': 'coma entre parametros',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 1
                        elif linea['contenido'][x] in (')'):
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif yest == 5:
                        if linea['contenido'][x] in (' '):
                            yest = 5
                        elif linea['contenido'][x] in (';'):
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif yest == 6:
                        if linea['contenido'][x].isdigit() or linea['contenido'][x] in ('.'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            yest = 6
                        elif linea['contenido'][x] in (' '):
                            yest = 6
                        elif linea['contenido'][x] in (','):
                            tokensTotales.append(tok)
                            tok = {'lexema': ',', 'token': 'tkn_coma', 'descripcion': 'coma entre parametros',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 1
                        elif linea['contenido'][x] in (')'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            yest = 5
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 11:
                    if fest == 0:
                        if linea['contenido'][x] in (' '):
                            fest = 0
                            print(linea['contenido'][x])
                        elif linea['contenido'][x].isalpha() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_identificador'
                            tok['descripcion'] = 'identificador como parametro de funcion'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            fest = 1
                        elif linea['contenido'][x] in (')'):
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 2
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 1:
                        if linea['contenido'][x].isalpha() or linea['contenido'][x].isdigit() or linea['contenido'][x] in ('_'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            fest = 1
                        elif linea['contenido'][x] in (','):
                            print(linea['contenido'][x])
                            tokensTotales.append(tok)
                            tok = {'lexema': ',', 'token': 'tkn_coma', 'descripcion': 'coma entre parametros de una funcion',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 0
                        elif linea['contenido'][x] in (')'):
                            tokensTotales.append(tok)
                            print(linea['contenido'][x])
                            tok = {'lexema': ')', 'token': 'tkn_parentesis_cerrado', 'descripcion': 'parentesis cerrado en una funcion',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 2
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 2:
                        if linea['contenido'][x] in (' '):
                            fest = 2
                            print(linea['contenido'][x])
                        elif linea['contenido'][x] in ('='):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_flecha'
                            tok['descripcion'] = 'singo de funcion de flecha'
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            fest = 3
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 3:
                        if linea['contenido'][x] in ('>'):
                            print(linea['contenido'][x])
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 4
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                    elif fest == 4:
                        if linea['contenido'][x] in (' '):
                            print(linea['contenido'][x])
                            fest = 4
                        elif linea['contenido'][x] in ('{'):
                            print(linea['contenido'][x])
                            tok = {'lexema': '{', 'token': 'tkn_llave_abierta', 'descripcion': 'llave abierta de funcion',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            fest = 0
                            e = 0
                        else:
                            error = {'linea': linea['linea'], 'columna': x+1}
                            errores.append(error)
                            print('hubo un error')
                elif e == 12:
                    if scest == 0:
                        if linea['contenido'][x] in ('s'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            scest = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            e = 10
                            scest = 0
                    elif scest == 1:
                        if linea['contenido'][x] in ('e'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            scest = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            e = 10
                            scest = 0
                    elif scest == 2:
                        if linea['contenido'][x] in (' '):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['token'] = 'tkn_case'
                            tok['descripcion'] = 'palabra reservada case'
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            scest = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            e = 10
                            scest = 0
                    elif scest == 3:
                        if linea['contenido'][x].isdigit():
                            tok['lexema'] = tok['lexema'] = linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_case_numero'
                            tok['descripcion'] = 'numero de case'
                            scest = 3
                        elif linea['contenido'][x].isalpha():
                            scest = 4
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                        elif linea['contenido'][x] in ('\"'):
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            scest = 5
                        elif linea['contenido'][x] in (' '):
                            scest = 3
                        elif linea['contenido'][x] in (':'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ':', 'token': 'tkn_dos_puntos', 'descripcion': 'dos puntos para case',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            scest = 0
                            e = 0
                    elif scest == 4:
                        if linea['contenido'][x].isalpha():
                            scest = 4
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                        elif linea['contenido'][x] in (' '):
                            scest = 4
                        elif linea['contenido'][x] in (':'):
                            tokensTotales.append(tok)
                            tok = {'lexema': ':', 'token': 'tkn_dos_puntos', 'descripcion': 'dos puntos para case',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            scest = 0
                            e = 0
                    elif scest == 5:
                        if not linea['contenido'][x] in ('\"'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            tok['linea'] = linea['linea']
                            tok['columna'] = x + 1
                            tok['token'] = 'tkn_cadena_texto'
                            tok['descripcion'] = 'cadena de texto'
                            scest = 5
                        elif linea['contenido'][x] in ('\"'):
                            tokensTotales.append(tok)
                            tok = {'lexema': '\"', 'token': 'tkn_comillas_dobles', 'descripcion': 'comillas dobles',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            scest = 6
                    elif scest == 6:
                        if linea['contenido'][x] in (':'):
                            tok = {'lexema': ':', 'token': 'tkn_dos_puntos', 'descripcion': 'dos puntos para case',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            scest = 0
                            e = 0

                elif e == 13:
                    if sbest == 0:
                        if linea['contenido'][x] in ('r'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 1
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 0
                            e = 10
                    elif sbest == 1:
                        if linea['contenido'][x] in ('e'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 2
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 0
                            e = 10
                    elif sbest == 2:
                        if linea['contenido'][x] in ('a'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 3
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 0
                            e = 10
                    elif sbest == 3:
                        if linea['contenido'][x] in ('k'):
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 4
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 0
                            e = 10
                    elif sbest == 4:
                        if linea['contenido'][x] in (';'):
                            tok['token'] = 'tkn_break'
                            tok['descripcion'] = 'palabra reservada break'
                            tokensTotales.append(tok)
                            tok = {'lexema': ';', 'token': 'tkn_punto_coma', 'descripcion': 'punto y coma',
                            'linea': linea['linea'], 'columna': x + 1}
                            tokensTotales.append(tok)
                            tok = {'lexema': '', 'token': '', 'descripcion': '', 'linea': '', 'columna': ''}
                            sbest = 0
                            e = 0
                        else:
                            tok['lexema'] = tok['lexema'] + linea['contenido'][x]
                            sbest = 0
                            e = 10

                
        #print(tokensTotales)
        #print(errores)
        self.tokens = tokensTotales
        self.errores = errores   
