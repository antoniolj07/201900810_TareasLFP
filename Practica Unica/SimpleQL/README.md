# Manual de Usuario
SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola,
su propósito es facilitar al usuario la búsqueda de registros completos en archivos
json, en los que buscar registro por registro podría ser muy tedioso y cansado. No
es el objetivo de SimpleQL convertirse en una versión de SQL, en su lugar, SimpleQL
funciona como una versión minimalista con algunas similitudes que permiten al
usuario cargar información a memoria por medio de comandos y obtener algunos
datos generales acerca de esta, como el número de registros, el valor máximo de un
atributo o incluso un reporte de en html de un conjunto de registros.


Para poder usar SimpleQL es necesario utilizar comandos específicos que tienen
distintas funciones:

* Cargar: Este comando permite la carga de diferentes archivos a memoria, el
único parámetro que lo conforma es una lista de direcciones a los archivos
que cargará a memoria. 
```
    CARGAR archivo1, archivo2, archivo3, …… archivoN
```

* Seleccionar: Permite seleccionar uno o más registros o atributos de estos
con base en condiciones simples que pueden aplicarse a los atributos de los
mismos.
```
    SELECCIONAR *
    SELECCIONAR nombre, edad DONDE promedio = 14.45
```

* Máximo: Permite encontrar el valor máximo que se encuentre en el atributo de
uno de los registros del conjunto en memoria. 
```
    MAXIMO edad
    MAXIMO promedio
```

* Permite encontrar el valor mínimo que se encuentre en el atributo
de uno de los registros del conjunto en memoria. 
```
    MINIMO edad
    MINIMO promedio
```

* Suma: Permite obtener la suma de todos los valores de un atributo
especificado en el comando. 
```
    SUMA edad
    SUMA promedio
```

* Cuenta: Permite contar el número de registros que se han cargado a
memoria.
```
     CUENTA
```

* Reportar: Este comando permite crear un reporte en html que contiene N
cantidad de registros. 
```
    REPORTAR N
```