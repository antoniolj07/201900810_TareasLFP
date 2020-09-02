import re
from components.commands.cargar import Cargar 
from components.commands.seleccionar import Seleccionar
from components.commands.maximo import Maximo
from components.commands.minimo import Minimo
from components.commands.suma import Suma
from components.commands.cuenta import Cuenta
from components.commands.reportar import Reportar

class Menu:

    archivos = []
    data = []
    def __init__(self):
        print('''
===================================
Listo para utilizar SimpleQL
===================================
        ''')
        self.corriendo = True
        self.comando()

    def comando(self):
        while self.corriendo != False:
            text = input()
            self.text = text
            command = re.split('\s', self.text)
            self.command = command
            if (self.command[0].lower() == 'cargar'):
                self.comando_cargar()
            elif (self.command[0].lower() == 'seleccionar'):
                self.comando_seleccionar()
            elif (self.command[0].lower() == 'maximo'):
                self.comando_maximo()
            elif (self.command[0].lower() == 'minimo'):
                self.comando_minimo()
            elif (self.command[0].lower() == 'suma'):
                self.comando_suma()
            elif (self.command[0].lower() == 'cuenta'):
                self.comando_cuenta()
            elif (self.command[0].lower() == 'reportar'):
                self.comando_reportar()
            elif (self.command[0].lower() == 'salir'):
                self.corriendo = False
            else:
                print('No se conoce ningun comando de tipo: ', self.command[0])



        

    def ver_archivos(self):
        separado = re.split('cargar ', self.text)
        paths = re.split(', ', separado[1])
        newPaths = []
        for path in paths:
            newPaths.append(path.replace('\'', ''))
        return newPaths

 
    def comando_cargar(self):
        paths = self.ver_archivos()
        car = Cargar(paths)
        self.archivos = car.archivosCargados
        self.data = car.contenido
        print('===============================================================================')
        for archivo in self.archivos:
            print('Nombre: {}, Edad: {}, Activo: {}, Promedio: {}'.format(archivo.nombre, archivo.edad, archivo.activo, archivo.promedio))
        print('===============================================================================')
    
    def comando_seleccionar(self):
        if (self.data):
            seleccion = Seleccionar(self.data, self.text)
            if (len(seleccion.infoFinal) != 0):
                for info in seleccion.infoFinal:
                    print(info)
            else:
                print('No hay resultados para: ',seleccion.condiciones[1])
        else:
            print('No ha seleccionado ningun archivo json')
            
    def comando_maximo(self):
        if (self.data):
            max = Maximo(self.data, self.text)
            if (max.num != 0):
                print('El valor maximo de {} es : {}'.format(max.campo, max.num))
        else:
           print('No ha seleccionado ningun archivo json') 
    
    def comando_minimo(self):
        if (self.data):
            min = Minimo(self.data, self.text)
            if (min.num != 1000):
                print('El valor minimo de {} es : {}'.format(min.campo, min.num))
        else:
           print('No ha seleccionado ningun archivo json') 
    
    def comando_suma(self):
        if (self.data):
            suma = Suma(self.data, self.text)
            if (suma.num != 0):
                print('El valor de la suma de {} es : {}'.format(suma.campo, suma.num))
        else:
           print('No ha seleccionado ningun archivo json') 
    
    def comando_cuenta(self):
        if (self.archivos):
            cuenta = len(self.archivos)
            print('El numero de registros cargados es: ', cuenta)
        else:
            print('No ha seleccionado ningun archivo json') 
    
    def comando_reportar(self):
        if (self.archivos):
            rep = Reportar(self.archivos, self.text)
        else:
            print('No se ha encontrado ningun archivo json')
menu = Menu()