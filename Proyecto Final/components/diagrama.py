class Diagrama:
    def __init__(self, tokens):
        print('diagrama')
        self.tokens = tokens
        self.ordenarDiagrama()

    def ordenarDiagrama(self):
        instrucciones = []
        for token in self.tokens:
            if not (token['token'] == 'tkn_diagonal_asterisco' or token['token'] == 'tkn_contenido_comentario' or token['token'] == 'tkn_asterisco_diagonal'):
                instrucciones.append(token)

        bloques = []
        contenido = {
            'tipo': '',
            'nombre': '',
            'valor': '',
            'condiciones': [],
            'parametros': [],
            'instrucciones': ['', '', '', '', '', '', '', '', '', '']
        }
        case = {'tipo': '', 'condicion': '', 'instrucciones': []}
        nuevoBloque = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
        e = 0
        i = 0
        llaves = 0
        for token in instrucciones:
            tkn = token['token']
            if e == 0:
                if tkn in ('tkn_identificador_funcion'):
                    print(tkn)
                    if llaves == 0:
                        contenido['tipo'] = 'llamada funcion'
                        contenido['nombre'] = token['lexema']
                    else:
                        nuevoBloque['tipo'] = 'llamada funcion'
                        nuevoBloque['nombre'] = token['lexema']
                    e = 1
                elif tkn in ('tkn_let') or tkn in ('tkn_var') or tkn in ('tkn_const'):
                    print(tkn)
                    if llaves == 0:
                        contenido['tipo'] = 'asignacion variable'
                    else:
                        nuevoBloque['tipo'] = 'asignacion variable'
                    e = 2
                elif tkn in ('tkn_llave_cerrada'):
                    print(tkn)
                    if llaves == 1:
                        bloques.append(contenido)
                        contenido = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
                    elif llaves == 2:
                        contenido['instrucciones'][llaves] = nuevoBloque
                        nuevoBloque = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
                    e = 0
                    llaves = llaves - 1
            elif e == 1:
                if tkn in ('tkn_identificador') or tkn in ('tkn_cadena_texto') or tkn in ('tkn_false') or tkn in ('tkn_true'):
                    print(tkn)
                    if llaves == 0:
                        contenido['parametros'].append(token['lexema'])
                    else:
                        nuevoBloque['parametros'].append(token['lexema'])
                    e = 1
                elif tkn in ('tkn_punto_coma'):
                    print(tkn)
                    if llaves == 0:
                        bloques.append(contenido)
                        contenido = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
                    else:
                        contenido['instrucciones'][llaves] = nuevoBloque
                        nuevoBloque = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
                    e = 0
            elif e == 2:
                if i == 0:
                    if tkn in ('tkn_identificador'):
                        print(tkn)
                        if llaves == 0:
                            contenido['nombre'] = token['lexema']
                        else:
                            nuevoBloque['nombre'] = token['lexema']
                        i = 1
                elif i == 1:
                    if tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        e = 3
                        i = 0
                    elif tkn in ('tkn_true') or tkn in ('tkn_false') or tkn in ('tkn_cadena_texto') or tkn in ('tkn_numero'):
                        print(tkn)
                        if llaves == 0:
                            contenido['valor'] = token['lexema']
                            bloques.append(contenido)
                            contenido = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
                        else:
                            nuevoBloque['valor'] = token['lexema']
                            contenido['instrucciones'][llaves] = nuevoBloque
                            nuevoBloque = {'tipo': '', 'nombre': '', 'valor': '', 'condiciones': [], 'parametros': [], 'instrucciones': ['', '', '', '', '', '', '', '', '', '']}
                        e = 0
                        i = 0
            elif e == 3:
                if i == 0:
                    if tkn in ('tkn_identificador'):
                        if llaves == 0:
                            contenido['parametros'].append(token['lexema'])
                        else:
                            nuevoBloque['parametros'].append(token['lexema'])
                        i = 0
                    elif tkn in ('tkn_llave_abierta'):
                        llaves = llaves + 1
                        i = 0
                        e = 0


        for bloque in bloques:
            tipo = bloque['tipo']
            nombre = bloque['nombre']
            valor = bloque['valor']      
            condiciones = bloque['condiciones']
            parametros = bloque['parametros']
            instrucciones = bloque['instrucciones']
            print('{} --- {} --- {} --- {} --- {} --- {}'.format(tipo, nombre, valor, condiciones, parametros, instrucciones))
            

