class Videojuego:
    def __init__(self, titulo='Defecto', HorasEsti=10, Entregado=False, genero='Base',compañia='Ninguno'):
        self.titulo=titulo
        self.HorasEsti=HorasEsti
        self.Entregado=Entregado
        self.genero=genero
        self.compañia=compañia


    def getTitulo(self):
        return self.titulo
    def getHorasEsti(self):
        return self.HorasEsti
    def getGenero(self):
        return self.genero
    def getCompañia(self):
        return self.compañia


    def setTitulo(self, titulo):
        self.titulo = titulo
    def setHorasEsti(self, HorasEsti):
        self.HorasEsti = HorasEsti
    def setGenero(self, genero):
        self.genero = genero
    def setCompañia(self, compañia):
        self.compañia = compañia

    def entregar(self):
        self.Entregado=True

    def devolver(self):
        self.Entregado=False

    def isEntregado(self):
        if self.Entregado == True :
            return True
        else :
            return False

    def toString(self):
        print('')
        print('Titulo: ' + self.titulo)
        print('Horas Estimadas: ' + str(self.HorasEsti))
        print('Entregado: ' + self.entregado())
        print('Genero: ' + self.genero)
        print('Compañia' +self.compañia)
        print('')