import re

class Automata:
    cadena = '''(
        <
            [atributo_numerico] = 45.09,
            [atributo_cadena] = "hola mundo",
            [atributo_booleano] = true
        >,
        <
            [atributo_numerico] = 4,
            [atributo_cadena] = "adios mundo",
            [atributo_booleano] = false
        >,
        <
            [atributo_numerico] = -56.4,
            [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
            [atributo_booleano] = false
            >
    )'''
    def __init__(self):
        print(self.cadena.replace(' ', '').replace('\n', ''))
        self.cad = self.cadena.replace(' ', '').replace('\n', '')
        self.auto(self.cad)
    
    def auto(self, cadena):
        estado = 0
        for c in range(len(cadena)):
            if estado == 0:
                if cadena[c] in ('('):
                    print(cadena[c]+' - tkn_parentesis')
                    estado = 1
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 1:
                if cadena[c] in ('<'):
                    print(cadena[c]+' - tkn_menor_que')
                    estado = 2
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 2:
                if cadena[c] in ('['):
                    print(cadena[c]+' - tkn_corchete')
                    estado = 3
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 3:
                if cadena[c] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', '_'):
                    print(cadena[c]+' - tkn_texto')
                    estado = 3
                elif cadena[c] in (']'):
                    print(cadena[c]+' - tkn_corchete')
                    estado = 4
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 4:
                if cadena[c] in ('='):
                    print(cadena[c]+' - tkn_signo_igual')
                    estado = 5
                else: 
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 5:
                if cadena[c] in ('1','2','3','4','5','6','7','8','9','0','-','+'):
                    print(cadena[c]+' - tkn_inicio_de_numero')
                    estado = 6
                else:
                    print('posicion {} es invalida'.format(c))
                    return
            elif estado == 6:
                if cadena[c] in ('1','2','3','4','5','6','7','8','9','0','.'):
                    print(cadena[c]+' - tkn_numero')
                    estado = 6
                elif cadena[c] in (','):
                    print(cadena[c]+' - tkn_coma')
                    estado = 7
                else:
                    print('posicion {} es invalida'.format(c))
                    return
            elif estado == 7:
                if cadena[c] in ('['):
                    print(cadena[c]+' - tkn_corchete')
                    estado = 8
                else:
                    print('posicion {} es invalida'.format(c))
                    return
            elif estado == 8:
                if cadena[c] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', '_'):
                    print(cadena[c] +' - tkn_texto')
                    estado = 8
                elif cadena[c] in (']'+' - tkn_corchete'):
                    print(cadena[c])
                    estado = 9
                else:
                    print('posicion {} es invalida'.format(c))
                    return
            elif estado == 9:
                if cadena[c] in ('='):
                    print(cadena[c]+' - tkn_signo_igual')
                    estado = 10
                else: 
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 10:
                if cadena[c] in ('\"'):
                    print(cadena[c]+' - tkn_comillas_dobles')
                    estado = 11
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 11:
                if cadena[c] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',','):
                    print(cadena[c]+' - tkn_texto')
                    estado = 11
                elif cadena[c] in ('\"'):
                    print(cadena[c]+' - tkn_comilla')
                    estado = 12
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 12:
                if cadena[c] in (','):
                    print(cadena[c]+' - tkn_coma')
                    estado = 13
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 13:
                if cadena[c] in ('['):
                    print(cadena[c]+' - tkn_corchete')
                    estado = 14
                else:
                    print('posicion {} es invalida'.format(c))
                    return
            elif estado == 14:
                if cadena[c] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', '_'):
                    print(cadena[c]+' - tkn_texto')
                    estado = 14
                elif cadena[c] in (']'):
                    print(cadena[c]+' - tkn_corchete')
                    estado = 15
                else:
                    print('posicion {} es invalida'.format(c))
                    return
            elif estado == 15:
                if cadena[c] in ('='):
                    print(cadena[c]+' - tkn_signo_igual')
                    estado = 16
                else: 
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 16:
                if cadena[c] in ('t','r','u','e','f','a','l','s','e'):
                    print(cadena[c]+' - tkn_booleano')
                    estado = 16
                elif cadena[c] in ('>'):
                    print(cadena[c]+' - tkn_mayor_que')
                    estado = 17
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return
            elif estado == 17:
                if cadena[c] in (','):
                    print(cadena[c]+' - tkn_coma')
                    estado = 1
                elif cadena[c] in (')'):
                    print(cadena[c]+' - tkn_parentesis')
                    print('fin')
                else:
                    print('posicion {} es INVALIDA'.format(c))
                    return






auto = Automata()