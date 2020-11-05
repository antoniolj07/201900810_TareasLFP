/* 
Hola este es un comentario de mierda
let - let para funciones
var - var para funciones
const - const para funciones
if
while
foreach
switch 
function
*/

let variable = true;
var _nombre = 'jorge';
const num_uno = 45;

if (false) {
    let _ifvar = false;
}

while (variable) {
    var _while_var = 'variable';
}

foreach(num in num_uno) {
    const neo_num = 0;
}

switch (num_uno) {
    case 1:
        funcion1(45, variable);
        break;

    case 2:
        funcion1(32, _nombre);
        break;

    default:
        funcion1('nombre', false)
        break;
}

const funcion1 = (_param1, param2) => {
    if (param2) {
        var cadena = 'jiji';
        const arreglo = 5;
        foreach(arr in arreglo) {
            while (arr) {
                switch (arr) {
                    case 1:
                        var adios = 'adios';
                        funky(adios, true)
                    case 2:
                        let boo = true;
                        break;
                }
            }
        }
    }
}

var funky = (num1, num2) => {
    while (num2) {
        funcion1(num1, true);
    }
}