class Select:
    def __init__(self, mensaje, nset):
        self.nset = nset
        self.afd_select(mensaje)
    
    def afd_select(self, mensaje):
        atributos = []
        condiciones = []
        conectores = []
        sEst = 0
        error = False
        terminado = False
        for x in range(len(mensaje)):
            if sEst == 0:
                if mensaje[x].lower() in ('s'):
                    sEst = 1
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 1:
                if mensaje[x].lower() in ('e'):
                    sEst = 2
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 2:
                if mensaje[x].lower() in ('l'):
                    sEst = 3
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 3:
                if mensaje[x].lower() in ('e'):
                    sEst = 4
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 4:
                if mensaje[x].lower() in ('c'):
                    sEst = 5
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 5:
                if mensaje[x].lower() in ('t'):
                    sEst = 6
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 6:
                nAtri = ''
                if mensaje[x] in (' '):
                    sEst = 6
                elif mensaje[x] in ('*'):
                    nAtri = '*'
                    atributos.append(nAtri)
                    sEst = 8
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    nAtri = nAtri + mensaje[x]
                    sEst = 7
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 7:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    nAtri = nAtri + mensaje[x]
                    sEst = 7
                elif mensaje[x] in (','):
                    atributos.append(nAtri)
                    sEst = 6
                elif mensaje[x] in (' '):
                    atributos.append(nAtri)
                    sEst = 8
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 8:
                if mensaje[x] in (' '):
                    sEst = 8
                elif mensaje[x].lower() in ('w'):
                    sEst = 9
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 9:
                if mensaje[x].lower() in ('h'):
                    sEst = 10
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 10:
                if mensaje[x].lower() in ('e'):
                    sEst = 11
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 11:
                if mensaje[x].lower() in ('r'):
                    sEst = 12
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 12:
                if mensaje[x].lower() in ('e'):
                    sEst = 13
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 13:
                nCondi = {
                    'atributo': '',
                    'valor': '',
                    'signo': '',
                    'tipo': ''
                }
                if mensaje[x] in (' '):
                    sEst = 13
                elif mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    nCondi['atributo'] = nCondi['atributo'] + mensaje[x]
                    sEst = 14
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 14:
                if mensaje[x].isalpha() or mensaje[x].isdigit() or mensaje[x] in ('_','-'):
                    nCondi['atributo'] = nCondi['atributo'] + mensaje[x]
                    sEst = 14
                elif mensaje[x] in (' '):
                    sEst = 14
                elif mensaje[x] in ('='):
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 15
                elif mensaje[x] in ('<','>'):
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 23
                elif mensaje[x] in ('!'):
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 24
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 23:
                if mensaje[x] in (' '):
                    sEst = 15
                elif mensaje[x] in ('='):
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 15
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 24:
                if mensaje[x] in ('='):
                    nCondi['signo'] = nCondi['signo'] + mensaje[x]
                    sEst = 15
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 15:
                if mensaje[x] in (' '):
                    sEst = 15
                elif mensaje[x] in ('\"'):
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    nCondi['tipo'] = 'string'
                    sEst = 16
                elif mensaje[x].isdigit() or mensaje[x] in ('-'):
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    nCondi['tipo'] = 'number'
                    if x == len(mensaje) - 1:
                        condiciones.append(nCondi)
                    sEst = 17
                elif mensaje[x].isalpha():
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    nCondi['tipo'] = 'boolean'
                    sEst = 18
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 16:
                if not mensaje[x] in ('\"'):
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    sEst == 16
                elif mensaje[x] in ('\"'):
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    condiciones.append(nCondi)
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 17:
                if (mensaje[x].isdigit() or mensaje[x] in ('.')):
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    if x == len(mensaje) - 1:
                        condiciones.append(nCondi)
                    sEst = 17
                elif mensaje[x] in (' '):
                    condiciones.append(nCondi)
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break 
            elif sEst == 18:
                if mensaje[x].lower() in ('t','r','u','e','f','a','l','s'):
                    nCondi['valor'] = nCondi['valor'] + mensaje[x]
                    if x == len(mensaje) - 1:
                        condiciones.append(nCondi)
                    sEst = 18
                elif mensaje[x] in (' '):
                    condiciones.append(nCondi)
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 19:
                conector = ''
                if mensaje[x].lower() in ('a'):
                    conector = conector + mensaje[x]
                    sEst = 20
                elif mensaje[x].lower() in ('o'):
                    conector = conector + mensaje[x]
                    sEst = 25
                elif mensaje[x].lower() in ('x'):
                    conector = conector + mensaje[x]
                    sEst = 26
                elif mensaje[x] in (' '):
                    sEst = 19
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 20:
                if mensaje[x].lower() in ('n'):
                    conector = conector + mensaje[x]
                    sEst = 21
                elif mensaje[x] in (' '):
                    sEst = 20
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 21:
                if mensaje[x].lower() in ('d'):
                    conector = conector + mensaje[x]
                    conectores.append(conector)
                    sEst = 22
                elif mensaje[x] in (' '):
                    sEst = 21
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 22:
                if mensaje[x].lower() in (' '):
                    sEst = 13
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 25:
                if mensaje[x].lower() in ('r'):
                    conector = conector + mensaje[x]
                    conectores.append(conector)
                    sEst = 22
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 26:
                if mensaje[x].lower() in ('o'):
                    conector = conector + mensaje[x]
                    sEst = 27
                else:
                    print('Entrada invalida')
                    error = True
                    break
            elif sEst == 27:
                if mensaje[x].lower() in ('r'):
                    conector = conector + mensaje[x]
                    conectores.append(conector)
                    sEst = 22
                else:
                    print('Entrada invalida')
                    error = True
                    break
            else:
                print('Entrada invalida')
                error = True
                break
        
        self.error = error
        if error:
            print('hubo error')
        else:
            self.atributos = atributos
            self.condiciones = condiciones
            self.conectores = conectores
            print(self.atributos)
            print(self.condiciones)
            print(self.conectores)
            self.seleccionar()

    def seleccionar(self):
        if len(self.nset['archivos']) > 0:
            resultados = []
            andCoincidencias1 = []
            andCoincidencias2 = []
            orCoincidencias = []
            xorCoincidencias = []
            sError = False
            for x in self.nset['archivos']:
                if len(self.conectores) == 0:
                    for c in self.condiciones:
                        if c['signo'] in ('='):
                            try:
                                if x[c['atributo']] in (c['valor']):
                                    if not self.atributos[0] in ('*'):
                                        resultado = {}
                                        for a in self.atributos:
                                            resultado[a] = x[a]
                                        resultados.append(resultado)
                                    else:
                                        resultados.append(x)
                            except:
                                print('No se encontro: ',c['atributo'])
                                sError = True
                                break
                        elif c['signo'] in ('<') and c['tipo'] in ('number'):
                            if not x[c['atributo']].lower() in ('null'):
                                try:
                                    if float(x[c['atributo']]) < float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            resultados.append(resultado)
                                        else:
                                            resultados.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                        elif c['signo'] in ('>') and c['tipo'] in ('number'):
                            if not x[c['atributo']].lower() in ('null'):
                                try:
                                    if float(x[c['atributo']]) > float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            resultados.append(resultado)
                                        else:
                                            resultados.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                        elif c['signo'] in ('>=') and c['tipo'] in ('number'):
                            if not x[c['atributo']].lower() in ('null'):
                                try:
                                    if float(x[c['atributo']]) >= float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            resultados.append(resultado)
                                        else:
                                            resultados.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                        elif c['signo'] in ('<=') and c['tipo'] in ('number'):
                            if not x[c['atributo']].lower() in ('null'):
                                try:
                                    if float(x[c['atributo']]) <= float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            resultados.append(resultado)
                                        else:
                                            resultados.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                        elif c['signo'] in ('!='):
                            if not x[c['atributo']].lower() in ('null'):
                                try:
                                    if x[c['atributo']] != c['valor']:
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            resultados.append(resultado)
                                        else:
                                            resultados.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                        else:
                            print('No se encontraron coincidencias papi')
                elif self.conectores[0].lower() in ('and','or','xor'):
                    i = 0
                    for c in self.condiciones:
                        if not x[c['atributo']].lower() in ('null'):
                            if c['signo'] in ('='):
                                try:
                                    if x[c['atributo']] in (c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            if i == 0:
                                                andCoincidencias1.append(resultado)
                                            else:
                                                andCoincidencias2.append(resultado)
                                        else:
                                            if i == 0:
                                                andCoincidencias1.append(x)
                                            else:
                                                andCoincidencias2.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                            elif c['signo'] in ('<') and c['tipo'] in ('number'):
                                try:
                                    if float(x[c['atributo']]) < float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            if i == 0:
                                                andCoincidencias1.append(resultado)
                                            else:
                                                andCoincidencias2.append(resultado)
                                        else:
                                            if i == 0:
                                                andCoincidencias1.append(x)
                                            else:
                                                andCoincidencias2.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                            elif c['signo'] in ('>') and c['tipo'] in ('number'):
                                try:
                                    if float(x[c['atributo']]) > float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            if i == 0:
                                                andCoincidencias1.append(resultado)
                                            else:
                                                andCoincidencias2.append(resultado)
                                        else:
                                            if i == 0:
                                                andCoincidencias1.append(x)
                                            else:
                                                andCoincidencias2.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                            elif c['signo'] in ('>=') and c['tipo'] in ('number'):
                                try:
                                    if float(x[c['atributo']]) >= float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            if i == 0:
                                                andCoincidencias1.append(resultado)
                                            else:
                                                andCoincidencias2.append(resultado)
                                        else:
                                            if i == 0:
                                                andCoincidencias1.append(x)
                                            else:
                                                andCoincidencias2.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                            elif c['signo'] in ('<=') and c['tipo'] in ('number'):
                                try:
                                    if float(x[c['atributo']]) <= float(c['valor']):
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            if i == 0:
                                                andCoincidencias1.append(resultado)
                                            else:
                                                andCoincidencias2.append(resultado)
                                        else:
                                            if i == 0:
                                                andCoincidencias1.append(x)
                                            else:
                                                andCoincidencias2.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                            elif c['signo'] in ('!='):
                                try:
                                    if x[c['atributo']] != c['valor']:
                                        if not self.atributos[0] in ('*'):
                                            resultado = {}
                                            for a in self.atributos:
                                                resultado[a] = x[a]
                                            if i == 0:
                                                andCoincidencias1.append(resultado)
                                            else:
                                                andCoincidencias2.append(resultado)
                                        else:
                                            if i == 0:
                                                andCoincidencias1.append(x)
                                            else:
                                                andCoincidencias2.append(x)
                                except:
                                    print('No se encontro {} para todos los registros'.format(c['atributo']))
                                    sError = True
                                    break
                            else:
                                print('No se encontraron coincidencias papi')
                                sError = True
                                break
                            i = i + 1
                else:
                    print('No se econtraron respuestas para: ', self.conectores[0])
                    sError = True
            if not sError:
                if len(self.conectores) > 0:
                    if self.conectores[0].lower() in ('and'):
                        for a in andCoincidencias1:
                            for a1 in andCoincidencias2:
                                if a == a1:
                                    resultados.append(a)
                    elif self.conectores[0].lower() in ('or'):
                        res = []
                        for a in andCoincidencias1:
                            res.append(a)
                        for a in andCoincidencias2:
                            res.append(a)
                        for x in res:
                            if not x in resultados:
                                resultados.append(x)
                    elif self.conectores[0].lower() in ('xor'):
                        res = []
                        for a in andCoincidencias1:
                            res.append(a)
                        for a in andCoincidencias2:
                            res.append(a)
                        for x in res:
                            if x in andCoincidencias1 and x in andCoincidencias2:
                                print('')
                            else:
                                resultados.append(x)
                        
                print(resultados)
                self.resultados = resultados
                            

        else:
            print('No se encontraron registros')
                                    

                
            