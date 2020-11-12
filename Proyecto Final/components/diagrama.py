from graph import Graph

class Diagrama:
    def __init__(self, tokens):
        print('diagrama')
        self.tokens = tokens
        self.generarDiagrama()

    def ordenarDiagrama(self, tokens):
        for token in tokens:
            if token['lexema'] == 'true':
                token['token'] = 'tkn_true'
                token['descripcion'] = 'palabra reservada true'
            elif token['lexema'] == 'false':
                token['token'] = 'tkn_false'
                token['descripcion'] = 'palabra reservada false'
        instrucciones = []
        for token in tokens:
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
        llavesAbiertas = 0
        llavesCerradas = 0
        cases = 0
        breaks = 0
        aSwitch = False
        for token in instrucciones:
            tkn = token['token']
            if i == 0:
                if tkn in ('tkn_let'):
                    print(tkn)
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 1
                elif tkn in ('tkn_var'):
                    print(tkn)
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 2
                elif tkn in ('tkn_const'):
                    print(tkn)
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 3
                elif tkn in ('tkn_if'):
                    print(tkn)
                    if not adentro:
                        bloque['nombre'] = 'Sentencia If'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 4
                elif tkn in ('tkn_while'):
                    print(tkn)
                    if not adentro:
                        bloque['nombre'] = 'Sentencia While'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 5
                elif tkn in ('tkn_switch'):
                    print(tkn)
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
                        bloque['nombre'] = 'Llamada'
                        bloque['identificador'] = token['lexema']
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 8
                elif tkn in ('tkn_case'):
                    print(tkn)
                    if not adentro:
                        bloque['nombre'] = 'Case'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 10
                elif tkn in ('tkn_default'):
                    print(tkn)
                    if not adentro:
                        bloque['nombre'] = 'Default'
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 11
                elif tkn in ('tkn_break'):
                    print(tkn)
                    if not adentro:
                        bloque['sentencia'].append(token)
                    else:
                        bloque['contenido'].append(token)
                    i = 12
                elif tkn in ('tkn_llave_cerrada'):
                    llavesCerradas = llavesCerradas + 1
                    print(tkn)
                    if llavesAbiertas == llavesCerradas:
                        bloques.append(bloque)
                        bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                        adentro = False
                        if aSwitch:
                            aSwitch = False
                    else:
                        bloque['contenido'].append(token)

                    
            elif i == 1:
                if e == 0:
                    if tkn in ('tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['identificador'] = token['lexema']
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_igual','tkn_signo_igual'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_false','tkn_true','tkn_numero'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                    elif tkn in ('tkn_comillas_dobles'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 4
                    elif tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 9
                elif e == 3:
                    if tkn in ('tkn_punto_coma'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['nombre'] = 'asignacion'
                            bloques.append(bloque)
                            bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                elif e == 4:
                    if tkn in ('tkn_cadena_texto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 5
                elif e == 5:
                    if tkn in ('tkn_comillas_dobles'):
                        print(tkn)
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
            elif i == 2:
                if e == 0:
                    if tkn in ('tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['identificador'] = token['lexema']
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_igual','tkn_signo_igual'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_comillas_dobles'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                    elif tkn in ('tkn_false','tkn_true','tkn_numero'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 5
                    elif tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 9
                elif e == 3:
                    if tkn in ('tkn_cadena_texto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 4
                elif e == 4:
                    if tkn in ('tkn_comillas_dobles'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 5
                elif e == 5:
                    if tkn in ('tkn_punto_coma'):
                        print(tkn)
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
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['identificador'] = token['lexema']
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_igual','tkn_signo_igual'):
                        print(tkn)
                        print('entra en const igual')
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_numero','tkn_true','tkn_false'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                    elif tkn in ('tkn_comillas_dobles'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 4
                    elif tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 9
                elif e == 3:
                    if tkn in ('tkn_punto_coma'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['nombre'] = 'asignacion'
                            bloques.append(bloque)
                            bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                elif e == 4:
                    if tkn in ('tkn_cadena_texto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 5
                elif e == 5:
                    if tkn in ('tkn_comillas_dobles'):
                        print(tkn)
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
            elif i == 4:
                if e == 0:
                    if tkn in ('tkn_parentesis_abierto'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_true','tkn_false','tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_parentesis_cerrado'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_llave_abierta'):
                        llavesAbiertas = llavesAbiertas + 1
                        print(tkn)
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
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_true','tkn_false','tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                            bloque['parametros'].append(token['lexema'])
                        else:
                            bloque['contenido'].append(token)
                        e = 2
                elif e == 2:
                    if tkn in ('tkn_parentesis_cerrado'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_llave_abierta'):
                        llavesAbiertas = llavesAbiertas + 1
                        print(tkn)
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
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_identificador'):
                        print(tkn)
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 2 
                elif e == 2:
                    if tkn in ('tkn_parentesis_cerrado'):
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 3
                elif e == 3:
                    if tkn in ('tkn_llave_abierta'):
                        llavesAbiertas = llavesAbiertas + 1
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                        adentro = True
                        aSwitch = True
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
                            bloque['parametros'].append(token['lexema'])
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
                        llavesAbiertas = llavesAbiertas + 1
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
                            if tkn in ('tkn_cadena_texto'):
                                bloque['parametros'].append('\"'+token['lexema']+'\"')
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
                            bloques.append(bloque)
                            bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
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
                        llavesAbiertas = llavesAbiertas + 1
                        print(tkn)
                        if not adentro:
                            bloque['nombre'] = 'definicion'
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)    
                        e = 0
                        i = 0
                        adentro = True
            elif i == 10:
                if e == 0:
                    if tkn in ('tkn_case_numero'):
                        print(tkn)
                        if not adentro:
                            bloque['parametros'].append(token['lexema'])
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 1
                elif e == 1:
                    if tkn in ('tkn_dos_puntos'):
                        cases = cases + 1
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                        adentro = True
            elif i == 11:
                if e == 0:
                    if tkn in ('tkn_dos_puntos'):
                        cases = cases + 1
                        print(tkn)
                        if not adentro:
                            bloque['sentencia'].append(token)
                        else:
                            bloque['contenido'].append(token)
                        e = 0
                        i = 0
                        adentro = True
            elif i == 12:
                if e == 0:
                    if tkn in ('tkn_punto_coma'):
                        print(tkn)
                        if not aSwitch:
                            if adentro:
                                bloques.append(bloque)
                                bloque = {'nombre': '', 'contenido': [], 'abierto': '', 'sentencia': [], 'parametros': [], 'identificador': ''}
                                adentro = False
                            else:
                                bloque['contenido'].append(token)
                        else:
                            bloque['contenido'].append(token)
                            
                        e = 0
                        i = 0
                
        return bloques

    def generarDiagrama(self):
        bloques = self.ordenarDiagrama(self.tokens)
        for bloque in bloques:
            if len(bloque['contenido']) > 0:
                nbloque1 = self.ordenarDiagrama(bloque['contenido'])
                bloque['contenido'] = nbloque1
                for bq in bloque['contenido']:
                    if len(bq['contenido']) > 0:
                        nbloque2 = self.ordenarDiagrama(bq['contenido'])
                        bq['contenido'] = nbloque2
                        for nbq in bq['contenido']:
                            if len(nbq['contenido']) > 0:
                                nbloque3 = self.ordenarDiagrama(nbq['contenido'])
                                nbq['contenido'] = nbloque3
                                for bloc in nbq['contenido']:
                                    if len(bloc['contenido']) > 0:
                                        nbloque4 = self.ordenarDiagrama(bloc['contenido'])
                                        bloc['contenido'] = nbloque4


        for bloque in bloques:
            sen = ''
            con = ''
            for token in bloque['sentencia']:
                sen = sen + token['token'] + ', '
            print('''
SENTENCIA:     {}
CONTENIDO:     {}
NOMBRE:        {}
PARAMETROS:    {}
IDENTIFICADOR: {}
==================================================================================================================
            '''.format(sen, bloque['contenido'], bloque['nombre'], bloque['parametros'], bloque['identificador']))

        gg = Graph(bloques)

