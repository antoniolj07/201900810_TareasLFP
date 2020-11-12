import dominate
from dominate.tags import *
import webbrowser
import os
class Pila:
    tokens = []
    def __init__(self, tokens):
        print('Inicio de Pila')
        for token in tokens:
            if token['lexema'] == 'true':
                token['token'] = 'tkn_true'
                token['descripcion'] = 'palabra reservada true'
            elif token['lexema'] == 'false':
                token['token'] = 'tkn_false'
                token['descripcion'] = 'palabra reservada false'

        for token in tokens:
            if not token['token'] in ('tkn_diagonal_asterisco','tkn_contenido_comentario','tkn_asterisco_diagonal'):
                self.tokens.append(token['token'])
                
        self.automataPila()

    def automataPila(self):
        tokens = self.tokens
        tokens.append('#')
        pila = []
        iteraciones = []
        iteracion = {
            'pila': '',
            'entrada': '',
            'trancision': []
        }
        iteracion = {'pila': ['$'], 'entrada': str(tokens), 'trancision': '(Io, $, $, p, #)'}
        iteraciones.append(iteracion)
        iteracion = {'pila': ['$'], 'entrada': tokens, 'trancision': '(Io, $, $, p, #)'}
        self.imp(iteracion)
        pila.append('$')
        input()
        i = 0   # Posicion de la entrada (lista de tokens)
        e = 1   # Estado del automata
        utlimoReemplazo = ''    # Ultimo reemplazo de simbolo no terminal
        while(len(pila) != 0):
            iterTerminado = False
            i = i + 1
            token = ''
            if len(tokens) > 0:
                token = tokens[0]
                
            p = len(pila) - 1
            if e == 1:
                if pila[0] in ('$'):
                    pila.pop()
                pila.append('#')
                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(p, $, $, q, S)'}
                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(p, $, $, q, S)'})
                self.imp(iteracion)
                e = 2
                iterTerminado = True
            elif e == 2:
                if token in pila[p]:
                    tokens.pop(0)
                    pila.pop()
                    iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, '+token+', '+token+', q, $)'}
                    iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, '+token+', '+token+', q, $)'})
                    self.imp(iteracion)
                    iterTerminado = True
                else:    
                    if pila[p] in ('#') and len(tokens) != 0:
                        pila.append('S')
                        iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(p, $, $, q, '+self.dicc(token)+')'}
                        iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(p, $, $, q, '+self.dicc(token)+')'})
                        self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('tkn_llave_cerrada') and not token in ('tkn_llave_cerrada'):
                        pila.append('S')
                        iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, $, q, '+self.dicc(token)+')'}
                        iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, $, q, '+self.dicc(token)+')'})
                        self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('S'):
                        pila.pop()
                        utlimoReemplazo = 'S'
                        if self.dicc(token) in ('SENTENCIA_VAR'):
                            pila.append('V')
                            pila.append('tkn_signo_igual')
                            pila.append('tkn_identificador')
                            pila.append('tkn_var')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, var id = V)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, var id = V)'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('LLAMADA_FUNCION'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('F')
                            pila.append('tkn_parentesis_abierto')
                            pila.append('tkn_identificador_funcion')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, idFuncion ( F ) ; )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, idFuncion ( F ) ; )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_LET'):
                            pila.append('L')
                            pila.append('tkn_igual')
                            pila.append('tkn_identificador')
                            pila.append('tkn_let')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, Let id = L)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, Let id = L)'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_CONST'):
                            pila.append('C')
                            pila.append('tkn_signo_igual')
                            pila.append('tkn_identificador')
                            pila.append('tkn_const')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, const id = C)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, const id = C)'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_IF'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('I')
                            pila.append('tkn_parentesis_abierto')
                            pila.append('tkn_if')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, if ( I ){ )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, if ( I ){ )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_WHILE'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('I')
                            pila.append('tkn_parentesis_abierto')
                            pila.append('tkn_while')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, while ( I ) { )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, while ( I ) { )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_FOREACH'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('tkn_identificador')
                            pila.append('tkn_in')
                            pila.append('tkn_elemento_identificador')
                            pila.append('tkn_parentesis_abierto')
                            pila.append('tkn_foreach')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, foreach ( id in id ) { )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, foreach ( id in id ) { )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_SWITCH'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('tkn_identificador')
                            pila.append('tkn_parentesis_abierto')
                            pila.append('tkn_switch')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, switch ( id ) { )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, switch ( id ) { )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_CASE'):
                            pila.append('S')
                            pila.append('tkn_dos_puntos')
                            pila.append('Z')
                            pila.append('tkn_case')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, case nun : )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, case nun : )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_DEFAULT'):
                            pila.append('S')
                            pila.append('tkn_dos_puntos')
                            pila.append('tkn_default')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, default : )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, default : )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif self.dicc(token) in ('SENTENCIA_BREAK'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_break')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, break ; )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, break ; )'})
                            self.imp(iteracion)
                            iterTerminado = True
                        elif token in ('tkn_llave_cerrada'):
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, S, q, $ )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, S, q, break ; )'})
                            self.imp(iteracion)
                            iterTerminado = True
                    elif pila[p] in ('V'):
                        pila.pop()
                        if token in ('tkn_comillas_dobles'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_comillas_dobles')
                            pila.append('tkn_cadena_texto')
                            pila.append('tkn_comillas_dobles')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, V, q, " cadena " ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, V, q, " cadena " ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_numero'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_numero')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, V, q, numero ; )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, C, q, numero )'})
                            self.imp(iteracion)
                        elif token in ('tkn_true') or token in ('tkn_false'):
                            pila.append('tkn_punto_coma')
                            pila.append('B')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, L, q, B ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, L, q, B ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_parentesis_abierto'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_flecha')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('P')
                            pila.append('tkn_parentesis_abierto')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, V, q, ( P ) { S } )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, V, q, ( P ) { S } )'})
                            self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('P'):
                        utlimoReemplazo = 'P'
                        pila.pop()
                        pila.append('tkn_identificador')
                        iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, P, q, id)'}
                        iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, P, q, id)'})
                        self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('L'):
                        pila.pop()

                        if token in ('tkn_comillas_dobles'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_comillas_dobles')
                            pila.append('tkn_cadena_texto')
                            pila.append('tkn_comillas_dobles')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, L, q, " cadena " ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, L, q, " cadena " ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_numero'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_numero')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, L, q, numero ; )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, L, q, numero )'})
                            self.imp(iteracion)
                        elif token in ('tkn_true') or token in ('tkn_false'):
                            pila.append('tkn_punto_coma')
                            pila.append('B')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, L, q, B ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, L, q, B ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_parentesis_abierto'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_flecha')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('P')
                            pila.append('tkn_parentesis_abierto')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, L, q, ( P ) { S } )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, L, q, ( P ) { S } )'})
                            self.imp(iteracion)
                        iterTerminado = True

                    elif pila[p] in ('B'):
                        utlimoReemplazo = 'B'
                        pila.pop()
                        pila.append('tkn_true')
                        iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, B, q, true )'}
                        iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, B, q, true )'})
                        self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('C'):
                        utlimoReemplazo = 'C'
                        pila.pop()

                        if token in ('tkn_comillas_dobles'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_comillas_dobles')
                            pila.append('tkn_cadena_texto')
                            pila.append('tkn_comillas_dobles')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, C, q, " cadena " ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, C, q, " cadena " ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_numero'):
                            pila.append('tkn_punto_coma')
                            pila.append('tkn_numero')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, C, q, numero ; )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, C, q, numero )'})
                            self.imp(iteracion)
                        elif token in ('tkn_true') or token in ('tkn_false'):
                            pila.append('tkn_punto_coma')
                            pila.append('B')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, C, q, B ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, C, q, B ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_parentesis_abierto'):
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_flecha')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('P')
                            pila.append('tkn_parentesis_abierto')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, C, q, ( P ) { S } )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, C, q, ( P ) { S } )'})
                            self.imp(iteracion)
                        iterTerminado = True

                    elif pila[p] in ('I'):
                        utlimoReemplazo = 'I'
                        pila.pop()
                        pila.append('tkn_identificador')
                        iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, I, q, id )'}
                        iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, I, q, id )'})
                        self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('F'):
                        utlimoReemplazo = 'F'
                        pila.pop()
                        pila.append('tkn_identificador')
                        iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, id )'}
                        iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, id )'})
                        self.imp(iteracion)
                        iterTerminado = True
                    elif pila[p] in ('Z'):
                        pila.pop()
                        if token in ('tkn_true','tkn_false'):
                            pila.append('B')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, Z, q, B ;)'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, Z, q, B ;)'})
                            self.imp(iteracion)
                        elif token in ('tkn_comillas_dobles'):
                            pila.append('tkn_comillas_dobles')
                            pila.append('tkn_cadena_texto')
                            pila.append('tkn_comillas_dobles')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, Z, q, " texto " )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, Z, q, " texto " )'})
                            self.imp(iteracion)
                        elif token in ('tkn_case_numero'):
                            pila.append('tkn_case_numero')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, Z, q, num )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, Z, q, num )'})
                            self.imp(iteracion)
                        iterTerminado = True
            if not iterTerminado:   
                if self.esTerminal(pila[p]) and len(token) > 0:
                    if not token in pila[p]:
                        if utlimoReemplazo in ('V'):
                            pila.pop()
                            pila.pop()
                            pila.pop()
                            pila.pop()
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_flecha')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('P')
                            pila.append('tkn_parentesis_abierto')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, V, q, ( P ) { )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, V, q, ( P ) { )'})
                            self.imp(iteracion)
                        elif utlimoReemplazo in ('P'):
                            if token in ('tkn_parentesis_cerrado'):
                                pila.pop()
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, P, q, , $ )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, P, q, , $ )'})
                                self.imp(iteracion)
                            else:
                                pila.append('tkn_identificador')
                                pila.append('tkn_coma')
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, P, q, , id )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, P, q, , id )'})
                                self.imp(iteracion)
                        elif utlimoReemplazo in ('L'):
                            pila.pop()
                            pila.pop()
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_flecha')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('P')
                            pila.append('tkn_parentesis_abierto')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, L, q, ( P ) { )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, L, q, ( P ) { )'})
                            self.imp(iteracion)
                        elif utlimoReemplazo in ('B'):
                            pila.pop()
                            pila.append('tkn_false')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, B, q, false )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, B, q, false )'})
                            self.imp(iteracion)
                            utlimoReemplazo = 'L'
                        elif utlimoReemplazo in ('C'):
                            pila.pop()
                            pila.pop()
                            pila.append('tkn_llave_cerrada')
                            pila.append('S')
                            pila.append('tkn_llave_abierta')
                            pila.append('tkn_flecha')
                            pila.append('tkn_parentesis_cerrado')
                            pila.append('P')
                            pila.append('tkn_parentesis_abierto')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, C, q, ( P ) { )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, C, q, ( P ) { )'})
                            self.imp(iteracion)
                        elif utlimoReemplazo in ('I'):
                            pila.pop()
                            pila.append('tkn_true')
                            iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, I, q, true )'}
                            iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, I, q, true )'})
                            self.imp(iteracion)
                            utlimoReemplazo = 'B'
                        elif utlimoReemplazo in ('F'):
                            if token in ('tkn_coma'):
                                pila.append('F')
                                pila.append('tkn_coma')
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, ,F )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, ,F )'})
                                self.imp(iteracion)
                            elif token in ('tkn_true'):
                                pila.pop()
                                pila.append('tkn_true')
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, true )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, true )'})
                                self.imp(iteracion)
                            elif token in ('tkn_false'):
                                pila.pop()
                                pila.append('tkn_false')
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, false )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, false )'})
                                self.imp(iteracion)
                            elif token in ('tkn_comillas_dobles'):
                                pila.pop()
                                pila.append('tkn_comillas_dobles')
                                pila.append('tkn_cadena_texto')
                                pila.append('tkn_comillas_dobles')
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, " texto " )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, " texto " )'})
                                self.imp(iteracion)
                            elif token in ('tkn_numero'):
                                pila.pop()
                                pila.append('tkn_numero')
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, numero )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, false )'})
                                self.imp(iteracion)
                            elif token in ('tkn_parentesis_cerrado'):
                                pila.pop()
                                iteracion = {'pila': pila, 'entrada': tokens, 'trancision': '(q, $, F, q, $ )'}
                                iteraciones.append({'pila': str(pila), 'entrada': str(tokens), 'trancision': '(q, $, F, q, $ )'})
                                self.imp(iteracion)

            input()
                
        print('Exitoo')
        self.generarHtml(iteraciones)

    def esTerminal(self, simbolo):
        terminal = True
        if simbolo in ('S','V','$','#','P'):
            terminal = False
        return terminal

    def dicc(self, token):
        terminal = ''
        if token in ('tkn_identificador_funcion'):
            terminal = 'LLAMADA_FUNCION'
        elif token in ('tkn_if'):
            terminal = 'SENTENCIA_IF'
        elif token in ('tkn_while'):
            terminal = 'SENTENCIA_WHILE'
        elif token in ('tkn_foreach'):
            terminal = 'SENTENCIA_FOREACH'
        elif token in ('tkn_let'):
            terminal = 'SENTENCIA_LET'
        elif token in ('tkn_const'):
            terminal = 'SENTENCIA_CONST'
        elif token in ('tkn_var'):
            terminal = 'SENTENCIA_VAR'
        elif token in ('tkn_switch'):
            terminal = 'SENTENCIA_SWITCH'
        elif token in ('tkn_case'):
            terminal = 'SENTENCIA_CASE'
        elif token in ('tkn_default'):
            terminal = 'SENTENCIA_DEFAULT'
        elif token in ('tkn_break'):
            terminal = 'BREAK'
        else:
            terminal = 'TERMINAL'
        return terminal

    def imp(self, iteracion):
        entrada = ''
        for token in iteracion['entrada']:
            entrada = entrada + token + ', '
        print('''
PILA       : {}
ENTRADA    : {}
TRANCISION : {}
==================================================================================================================================
'''.format(iteracion['pila'], entrada, iteracion['trancision']))


    def generarHtml(self, iteraciones):
        doc = dominate.document(title = 'pila')
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        with doc:
            with div( cls='container mt-5 mb-5'):
                h1('Pila')
                hr()
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Pila')
                            th('Entrada')
                            th('Trancision')
                    with tbody():
                        for iteracion in iteraciones:
                            pila = ''
                            entrada = ''
                            for elemento in iteracion['pila']:
                                pila = pila + elemento + ', '
                            for elemento in iteracion['entrada']:
                                entrada = entrada + elemento

                            with tr():
                                td(iteracion['pila'])
                                td(iteracion['entrada'])
                                td(iteracion['trancision'])

        with open('pages/pila.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)
        webbrowser.open_new_tab(os.path.abspath('pages/pila.html'))

