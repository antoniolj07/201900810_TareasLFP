# Gramática Utilizada

Para la elaboracion de este proyecto se utilizó una gramática que entra por el automata de pila para verificar si el archivo javascript pertenece al lenguaje. Esta gramática está conformada por simbolos terminales y no terminales. Los simbolos terminales son tokens que cuando coinciden con el token de entrada, se acepta la entrada y se quita un elemento de la pila. Los simbolos no terminales pueden ser equivalentes a uno o varios patrones de tokens que cambian dependiendo de la estructura de la entrada. Los simbolos no terminales estan conformados por:

*   S: En este apartado puede entrar cualquier inicio de sentencia que pertenezca al lenguaje.
*   V: Este símbolo puede ser sustituido para asignar valor de tipo cadena de texto a una variable o se puede declarar una función
*   C: Este símbolo puede ser sustituido para asignar valor de tipo numerico a una variablo o para declarar una función.
*   L: Este símbolo puede ser sustituido para asignar valor de tipo booleano a una variable o para declarar una función. 
*   F: Este símbolo se utiliza para recibir una cantidad indefinida de parametros en una declaración de función.
*   A: Este símboolo se utiliza para recibir una variable o valor booleano como condición de una sentencia if o while.
*   B: Este símbolo se utiliza para validar cualquier valor booleano, acepta de entrada true o false.
*   P: Este símbolo se utiliza para recibir una cantidad indefinida de parametros en una llamada a función.
*   W: Este símbolo se utiliza para validar el contenido de un switch, ya que este puede llevar una cantidad indefinida de cases y un default.
*   H: Este símbolo se utiliza para validar la estructura de un case dentro de un switch.
*   D: Este símbolo se utiliza para validar la estructura de un default dentro de un switch.

S ->

    |	tk_let tk_identificador tkn_signo_igual L

    |   tk_var tk_identificador tk_signo_igual  V 

    |	tk_const tk_identificador tk_sifno_igual C

    |	tk_if tk_parentesis_abierto A tk_parentesis_cerrado tk_llave_abierta S tk_llave_cerrada

    |	tk_while parentesis_abierto A tk_parentesis_cerrado tk_llave_abierta S tk_llave_cerrada

    |	tk_foreach parentesis_abierto tk_identificador_elemento tk_in tk_identificador tk_parentesis_cerrado tk_llave_abierta S tk_llave_cerrada

    |	tk_switch tk_parentesis_abierto tk_identificador tk_parentesis_cerrado tk_llave_abierta W tk_llave_cerrada

    |	tk_identificador_funcion tk_parentesis_abierto P tk_parentesis_cerrado tk_punto_coma

    |	ʎ


V ->

    |   tk_comillas_dobles tk_cadena_texto tk_comillas_dobles tk_punto_coma

    |	tk paréntesis F tk_parentesis_cerrado tk_flecha tk_llave_abierta S tk_llave_cerrada

L -> 

    |   B tk_punto_coma

    |	tk paréntesis F tk_parentesis_cerrado tk_flecha tk_llave_abierta S tk_llave_cerrada

C ->   

    |   tk_numero tk_punto_coma

    | 	tk paréntesis F tk_parentesis_cerrado tk_flecha tk_llave_abierta S tk_llave_cerrada

F ->	

    |   tk_identificador

    |	tk_coma F

    |	ʎ

A ->

    |   tk_identificador

    |	B

B -> 	

    |   tk_false

    |	tk_true

P -> 	

    |   tk_identificador

    |	B

    |	tk_comillas_dobles tk_cadena_texto tk_comillas_dobles

    |	tk_coma P

    |	ʎ

W -> 	

    |   H

    |	D

    |	ʎ

H ->

    |   tk_case tk_numero tk_dos_puntos S tk_break tk_punto_coma W

D ->

    |   tk_default tk_dos_puntos S tk_break tk_punto_coma
