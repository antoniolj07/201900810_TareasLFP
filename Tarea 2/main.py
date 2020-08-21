class Main:
    def __init__(self):
        print('=====================================')
        print('Ingrese la informacion que desea ver:')
        print('1-Heroes de Marvel con formato json')
        print('2-Heroes de DC con formato xml')
        print('3-Villanos de DC con formato csv')
        print('pulse cualquier otra cosa para salir')
        print('======================================')
        opcion = input()
        self.irData(opcion)
    
    def irData(self, opcion):
        print(opcion)
        if (opcion == '1'):
            import services.HeroesMarvel
        elif (opcion == '2'):
            import services.HeroesDc
        elif (opcion == '3'):
            import services.VillanosDc
        else:
            print('adios')
            return

ingreso = Main()