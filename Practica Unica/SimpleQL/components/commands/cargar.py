import json
import components.menu
from models.registro_model import Registro
class Cargar:
    archivosCargados = []
    def __init__(self, archivos):
        self.archivos = archivos
        self.verificar_archivos()
        
    def verificar_archivos(self):
        for archivo in self.archivos:
            try:
                with open(archivo) as data:
                    self.contenido = json.loads(data.read())
                    for registro in self.contenido:
                        try:
                            nombre = registro.get('nombre')
                            edad = registro.get('edad')
                            activo = registro.get('activo')
                            promedio = registro.get('promedio')
                            
                            persona = Registro(nombre, edad, activo, promedio)
                            self.archivosCargados.append(persona)
                        except:
                            print('El archivo no tiene la estructura json establecida')
            except:
                print('No se ha encontrado ningun archivo json en la ruta: ',archivo)
            
        