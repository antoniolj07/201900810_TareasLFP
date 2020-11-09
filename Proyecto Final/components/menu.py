from jsafd import JsAfd
from generaHtml import GeneraHtml
from diagrama import Diagrama
from pila import Pila

class Menu:
    tokens = []
    def __init__(self):
        self.verEntrada()
    
    def verEntrada(self):
        opcion = '0'
        while (opcion != '5'):
            print('''
=========> BIENVENIDO A BASILISK <=========
Seleccione una de las siguientes opciones
1 - Ingresar ruta de Script
2 - Generar registro de Tokens y Errores
3 - Generar Diagrama de Flujo
4 - Pila Interactiva
5 - Salir
            ''')
            opcion = input()
            
            if opcion == '1':
                self.irAfd()
            elif opcion == '2':
                self.irTokenError()
            elif opcion == '3':
                self.irDiagrama()
            elif opcion == '4':
                self.irPila()
            elif opcion == '5':
                print('Adios')
            else:
                print('Ingrese una opcion valida')
                


    def irAfd(self):
        ja = JsAfd()
        self.tokens = ja.tokens
        self.errores = ja.errores
    def irTokenError(self):
        if not len(self.tokens) == 0:
            print('Generar token y errores')
            gh = GeneraHtml(self.tokens, self.errores)
        else:
            print('No hay script seleccionado')
            

    def irDiagrama(self):
        if not len(self.tokens) == 0:
            diagrama = Diagrama(self.tokens)
        else:
            print('No hay script seleccionado')

    def irPila(self):
        if not len(self.tokens) == 0:
            pila = Pila(self.tokens)
        else:
            print('No hay tokens ingresados')

menu = Menu()