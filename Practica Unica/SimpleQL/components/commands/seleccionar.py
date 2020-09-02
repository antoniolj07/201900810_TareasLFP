import re
import json
from models.registro_model import Registro
class Seleccionar:
    def __init__(self, archivo, texto):
        self.archivo = archivo
        self.texto = texto
        self.ver_condiciones()
    

    def ver_condiciones(self):
        texto = re.split('\s', self.texto)
        for entrada in texto:
            if (entrada.lower() == 'donde'):
                try:
                    separado = re.split(texto[0].lower()+' ', self.texto)
                    palabras = re.split(' '+entrada+' ', separado[1])
                    self.campos = re.split(', ', palabras[0])
                    self.condiciones = re.split(' = ', palabras[1])
                except:
                    print('La estructura del comando es incorrecta')
        self.ver_condicion()

    def ver_condicion(self):
        self.infoCompleta = []
        for registro in self.archivo:
            try:
                if (float(self.condiciones[1])):
                    if (registro.get(self.condiciones[0]) == float(self.condiciones[1])):
                        persona = {
                            'nombre': registro.get('nombre'), 
                            'edad': registro.get('edad'),
                            'promedio': registro.get('promedio'),
                            'activo': registro.get('activo')      
                        }

                        self.infoCompleta.append(persona)
            except:
                if(self.condiciones[1].isdigit()):
                    if (registro.get(self.condiciones[0]) == int(self.condiciones[1])):
                        persona = {
                            'nombre': registro.get('nombre'), 
                            'edad': registro.get('edad'),
                            'promedio': registro.get('promedio'),
                            'activo': registro.get('activo')      
                        }

                        self.infoCompleta.append(persona)

                elif(self.condiciones[1].lower() == 'true' or self.condiciones[1].lower() == 'false'):
                    if(str(registro.get(self.condiciones[0].lower())).lower() == self.condiciones[1].lower()):
                        persona = {
                            'nombre': registro.get('nombre'), 
                            'edad': registro.get('edad'),
                            'promedio': registro.get('promedio'),
                            'activo': registro.get('activo')      
                        }

                        self.infoCompleta.append(persona)
                    
                    

                else:
                    if(self.condiciones[1][0] == '\'' and self.condiciones[1][len(self.condiciones[1])-1] == '\''):
                        condicion = re.split('\'', self.condiciones[1])
                        if(str(registro.get(self.condiciones[0])).lower() == condicion[1].lower()):
                            persona = {
                                'nombre': registro.get('nombre'), 
                                'edad': registro.get('edad'),
                                'promedio': registro.get('promedio'),
                                'activo': registro.get('activo')      
                            }

                            self.infoCompleta.append(persona)
                        
                    else:
                        if(registro.get(self.condiciones[0]).lower() == self.condiciones[1].lower()):
                            persona = {
                                'nombre': registro.get('nombre'), 
                                'edad': registro.get('edad'),
                                'promedio': registro.get('promedio'),
                                'activo': registro.get('activo')      
                            }

                            self.infoCompleta.append(persona)
        self.ver_campos()

    def ver_campos(self):
        self.infoFinal = []
        if (self.campos[0] == '*'):
            self.infoFinal = self.infoCompleta
        else: 
            for registro in self.infoCompleta:
                persona = []
                for campo in self.campos:
                    for key in registro:
                        if (campo == key):
                            persona.append(registro[key])
                self.infoFinal.append(persona)
        
    
