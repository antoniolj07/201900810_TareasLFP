import re
class Maximo:
    def __init__(self, archivo, texto):
        self.archivo = archivo
        self.texto = texto
        self.ver_campo()

    def ver_campo(self):
        separados = re.split('\s', self.texto)
        self.campo = separados[1]
        self.ver_maximo()

    def ver_maximo(self):
        self.num = 0
        esBool = False
        try:
            for iteracion in self.archivo:
                valor = iteracion.get(self.campo)
                if (str(valor).lower() != 'true' and str(valor).lower() != 'false'):
                    if (valor >= self.num):
                        self.num = valor
                else:
                    esBool = True
            if (esBool):
              print ('No se ha encontrado valores numericos para: ', self.campo)  
        except:
            print ('No se ha encontrado valores numericos para: ', self.campo)
        
        
