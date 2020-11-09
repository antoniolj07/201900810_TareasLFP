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
        
        adentro = False
        i = 0
        e = 0
        bloque = {
            'nombre': '',
            'contenido': [],
            'abierto': '',
            'sentencia': [],
            'parametros': [],
            'identificador': ''
        }
        for token in instrucciones:
            tkn = token['token']
            if i == 0:
                if tkn in ('tkn_let'):
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 1
                elif tkn in ('tkn_var'):
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 2
                elif tkn in ('tkn_const'):
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 3
                elif tkn in ('tkn_if'):
                    bloque['nombre'] = 'Sentenica If'
                    bloque['sentencia'].append(token)
                    i = 4
                elif tkn in ('tkn_while'):
                    if not adentro:
                        bloque['nombre'] = 'Sentencia While'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 5
                elif tkn in ('tkn_switch'):
                    if not adentro:
                        bloque['nombre'] = 'Sentencia Switch'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 6
                elif tkn in ('tkn_foreach'):
                    print(tkn)
                    if not adentro:
                        bloque['nombre'] = 'Sentencia Foreach'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 7
                elif tkn in ('tkn_identificador_funcion'):
                    print(tkn)
                    if not adentro:
                        bloque['nombre'] = 'Lamada'
                        bloque['identificador'] = token['lexema']
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 8
                elif tkn in ('tkn_llave_cerrada'):
                    bloques.append(bloque)
                    bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                    adentro = False
            elif i == 1:
                if e == 0:
                    if tkn in ('tkn_identificador'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['identificador'] = token['lexema']
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_igual','tkn_signo_igual'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_false','tkn_true'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                    elif tkn in ('tkn_parentesis_abierto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 9
                elif e == 3:
                    if tkn in ('tkn_punto_coma'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['nombre'] = 'asignacion'
                            bloques.append(bloque)
                            bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
            elif i == 2:
                if e == 0:
                    if tkn in ('tkn_identificador'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['identificador'] = token['lexema']
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_igual','tkn_signo_igual'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_comillas_dobles'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                    elif tkn in ('tkn_parentesis_abierto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 9
                elif e == 3:
                    if tkn in ('tkn_cadena_texto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 4
                elif e == 4:
                    if tkn in ('tkn_comillas_dobles'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 5
                elif e == 5:
                    if tkn in ('tkn_punto_coma'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['nombre'] = 'asignacion'
                            bloques.append(bloque)
                            bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
            elif i == 3:
                if e == 0:
                    if tkn in ('tkn_identificador'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['identificador'] = token['lexema']
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_igual','tkn_signo_igual'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_numero'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                    elif tkn in ('tkn_parentesis_abierto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 9
                elif e == 3:
                    if tkn in ('tkn_punto_coma'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['nombre'] = 'asignacion'
                            bloques.append(bloque)
                            bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
            elif i == 4:
                if e == 0:
                    if tkn in ('tkn_parentesis_abierto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_true','tkn_false','tkn_identificador'):
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_parentesis_cerrado'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_llave_abierta'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        adentro = True
                        e = 0
                        i = 0
            elif i == 5:
                if e == 0:
                    if tkn in ('tkn_parentesis_abierto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_true','tkn_false','tkn_identificador'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['parametros'].append(token['lexema'])
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_parentesis_cerrado'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_llave_abierta'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                        adentro = True
            elif i == 6:
                if e == 0:
                    if tkn in ('tkn_parentesis_abierto'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_identificador'):
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2 
                elif e == 2:
                    if tkn in ('tkn_parentesis_cerrado'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_llave_abierta'):
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                        adentro = True
            elif i == 7:
                if e == 0:
                    if tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_elemento_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_in'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 4
                elif e == 4:
                    if tkn in ('tkn_parentesis_cerrado'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 5
                elif e == 5:
                    if tkn in ('tkn_llave_abierta'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                        adentro = True
            elif i == 8:
                if e == 0:
                    if tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_identificador','tkn_true','tkn_false'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['parametros'].append(token['lexema'])
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                    elif tkn in ('tkn_comillas_dobles','tkn_cadena_texto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                    elif tkn in ('tkn_parentesis_cerrado'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_punto_coma'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
            elif i == 9:
                if e == 0:
                    if tkn in ('tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                    elif tkn in ('tkn_coma'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                    elif tkn in ('tkn_parentesis_cerrado'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_flecha'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_llave_abierta'):
                        print(tkn)
                        if not adentro:
                            bloque['nombre'] = 'definicion'
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)    
                        e = 0
                        i = 0
                        adentro = True
        self.generarDiagrama(bloques)

    def generarDiagrama(self, bloques):
        for bloque in bloques:
            sen = ''
            con = ''
            for token in bloque['sentencia']:
                sen = sen + token['token'] + ', '
            for token in bloque['contenido']:
                con = con + token['token'] + ','
            print('''
SENTENCIA:  {}
CONTENIDO:  {}
NOMBRE:     {}
PARAMETROS: {}
==================================================================================================================
            '''.format(sen, con, bloque['nombre'], bloque['parametros']))

