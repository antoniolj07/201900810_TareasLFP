# Manual de Usuario
SimpleQL CLI es un lenguaje de consultas que funciona únicamente a nivel de consola,
su propósito es facilitar al usuario la búsqueda de registros completos en archivos
json, en los que buscar registro por registro podría ser muy tedioso y cansado. No
es el objetivo de SimpleQL convertirse en una versión de SQL, en su lugar, SimpleQL
funciona como una versión minimalista con algunas similitudes que permiten al
usuario cargar información a memoria por medio de comandos y obtener algunos
datos generales acerca de esta, como el número de registros, el valor máximo de un
atributo o incluso un reporte de en html de un conjunto de registros.


Para poder usar SimpleQL CLI es necesario utilizar comandos específicos que tienen
distintas funciones:

* CREATE SET: Tiene la función de crear sets de memoria donde se alojarán ciertos conjuntos de
datos cargados por el usuario. La aplicación tiene la capacidad de poseer activos N
conjuntos de datos. 
```
    CREATE SET carros
```

* LOAD INTO set FILES file: Este comando carga al conjunto especificado por set_id la información contenida en
la los archivos de la lista de archivos definida después de la keyword FILES.
```
    LOAD INTO elementos FILES ejemplo1.aon, ejemplo2.aon....
    LOAD INTO carros FILES carros.aon
```

* USE SET setId: Este comando define el set de datos a utilizar para las siguientes operaciones, si se
intenta realizar operaciones sin haber definido un set de datos la aplicación debe
mostrar un error.
```
    USE SET carros
    USET SET elementos
```

* SELECT: Permite seleccionar uno o más registros o atributos de los mismos con base en
condiciones simples que pueden aplicarse a los atributos de los mismos.
En lugar de listar los atributos también es posible utilizar el operador *, esto
automáticamente seleccionará todos los campos del registro.
Ya que la estructura de los sets no está predefinida, sino que viene definida en los
archivos los atributos seleccionables serán cualquiera que pertenezca al set sobre el
cual se está actualmente trabajando.
```
    SELECT modelo, tipo, marca, año WHERE color = “rojo”
    SELECCIONAR *
    SELECCIONAR * WHERE marca = “Mazda” AND año < 1996
```

* LIST ATTRIBUTES: Este comando permite listar los atributos que componen a cada registro del set. 
```
    LIIST ATTRIBUTES
```

* PRINT IN: Este comando permite al usuario elegir el color en el que serán presentados los
resultados en la línea de comandos. Los valores a elegir serán BLUE, RED, GREEN,
YELLOW, ORANGE y PINK.
```
     PRINT IN PINK
```

* MAX | MIN: Permiten encontrar el valor máximo o el valor mínimo que se encuentre en el
atributo de uno de los registros del conjunto en memoria. En caso de seleccionar el
valor máximo de un valor de tipo String la comparación será realizada de forma
lexicográfica.
```
    MAX año
    MIN modelo
```
* SUM: Permite obtener la suma de todos los valores de un atributo especificado en el
comando. Este comando solamente se utilizará sobre valores de tipo numérico, no
se realizarán sumas sobre valores de tipo cadena o booleanos. En caso de
seleccionarse varios atributos deberá reportar cada atributo con su respectiva
suma, en caso de que el atrbuto tenga valor null se ignorara. 
```
    SUM edad, promedio, faltas
    SUM asistencias
```
* COUNT: Permite contar el número de registros que se han cargado a memoria. En caso de
que alguno de los atributos tenga valor null se ignorará. El comando COUNT
permite el uso del operador *.
```
    COUNT *
    COUNT edad, promedio, faltas
```
* REPORT TO: Este comando permite crear un reporte en html a partir de cualquier otro comando
de análisis o selección. El reporte debe ser agradable a la vista y fácil de leer. El id
define el nombre del archivo sobre el que se crea el reporte. 
```
    REPORT TO reporte1 COUNT *
    REPORT TO reporte2 SUM *
    REPORT TO reporte3 SELECT * WHERE edad != 44
```
* SCRIPT: Este comando permite cargar scripts con extensión .siql que contienen series de
instrucciones y comandos SimpleQL, esto con el objetivo de que el usuario no tenga
que escribir uno por uno los comandos que se desee ejecutar.
```
    SCRIPT archivo1.siql, archivo2.siql
```
* REPORT TOKENS: Este comando crea un reporte en html que muestra una lista de todos los
lexemas encontrados por el AFD, mostrando también a cual token pertenece
el lexema y una breve descripción del mismo.
```
    REPORT TOKENS
```