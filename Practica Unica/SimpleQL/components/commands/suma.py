import re
class Suma:
    def __init__(self, archivo, texto):
        self.archivo = archivo
        self.texto = texto
        self.ver_campo()
        
    def ver_campo(self):
        separados = re.split('\s', self.texto)
        self.campo = separados[1]
        self.ver_suma()

    def ver_suma(self):
        self.num = 0
        esBool = False
        try:
            for iteracion in self.archivo:
                valor = iteracion.get(self.campo)
                if (str(valor).lower() != 'true' and str(valor).lower() != 'false'):
                    self.num += valor
                else:
                    esBool = True
            if (esBool):
                print ('No se ha encontrado valores numericos para: ', self.campo)
        except:
            print ('No se ha encontrado valores numericos para: ', self.campo)