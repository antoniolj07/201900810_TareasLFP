class Token:
    lexema = ''
    token = ''
    descripcion = ''
    linea = ''
    columna = ''
    def  __init__(self, lexema, token, descripcion, linea, columna):
        self.lexema = lexema
        self.token = token
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
