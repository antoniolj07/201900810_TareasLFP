class AfdAon:
    def __init__(self, archivos):
        self.afd(archivos)

    def afd(self, archivos):
        registros = []
        error = False
        for archivo in archivos:
            contenido = ''
            try:
                with open (archivo, 'r') as f:
                    lineas = f.readlines()
                    for linea in lineas:
                        contenido = contenido + linea.strip()
            except:
                print('No se pudo leer el archivo ', archivo)

            if len(contenido) > 1:
                e = 0
                for x in range(len(contenido)):
                    if e == 0:
                        if contenido[x] in ('('):
                            e = 1
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 1:
                        if contenido[x] in (' '):
                            e = 1
                        elif contenido[x] in ('<'):
                            registro = {}
                            e = 2
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 2:
                        if contenido[x] in (' '):
                            e = 2
                        elif contenido[x] in ('['):
                            e = 3
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 3:
                        atributo = ''
                        if contenido[x] in (' '):
                            e = 3
                        elif contenido[x].isalpha() or contenido[x].isdigit() or contenido[x] in ('_','-'):
                            e = 4
                            atributo = atributo + contenido[x]
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 4:
                        if contenido[x].isalpha() or contenido[x].isdigit() or contenido[x] in ('_','-'):
                            e = 4
                            atributo = atributo + contenido[x]
                        elif contenido[x] in (']'):
                            registro[atributo] = ''
                            e = 5
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 5:
                        if contenido[x] in (' '):
                            e = 5
                        elif contenido[x] in ('='):
                            e = 6
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 6:
                        valor = ''
                        if contenido[x] in (' '):
                            e = 6
                        elif contenido[x] in ('\"'):
                            e = 7
                        elif contenido[x].isdigit() or contenido[x] in ('-'):
                            valor = valor + contenido[x]
                            e = 11
                        elif contenido[x].lower() in ('t','f'):
                            valor = valor + contenido[x]
                            e = 12
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 7:
                        if not contenido[x] in ('\"'):
                            valor = valor + contenido[x]
                            e = 7
                        elif contenido[x] in ('\"'):
                            e = 8
                            registro[atributo] = valor
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 8:
                        if contenido[x] in (' '):
                            e = 8
                        elif contenido[x] in (','):
                            e = 2
                        elif contenido[x] in ('>'):
                            registros.append(registro)
                            e = 9
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 9:
                        if contenido[x] in (','):
                            e = 1
                        elif contenido[x] in (' '):
                            e = 9
                        elif contenido[x] in (')'):
                            e = 10
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 10:
                        if contenido[x] in (' '):
                            e = 10
                        elif contenido[x] in (','):
                            e = 0
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 11:
                        if contenido[x].isdigit() or contenido[x] in ('.'):
                            valor = valor + contenido[x]
                            e = 11
                        elif contenido[x] in (','):
                            registro[atributo] = valor
                            e = 2
                        elif contenido[x] in ('>'):
                            registro[atributo] = valor
                            registros.append(registro)
                            e = 9
                        elif contenido[x] in (' '):
                            e = 11
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
                    elif e == 12:
                        if contenido[x].lower() in ('t','r','u','e','f','a','l','s','e'):
                            valor = valor + contenido[x]
                            e = 12
                        elif contenido[x] in (' '):
                            e = 12
                        elif contenido[x] in (','):
                            registro[atributo] = valor
                            e = 2
                        elif contenido[x] in ('>'):
                            registro[atributo] = valor
                            registros.append(registro)
                            e = 9
                        else:
                            print('El archivo no tiene la estructura necesaria')
                            error = True
                            break
        self.registros = registros
                

