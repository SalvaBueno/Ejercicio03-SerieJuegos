class Serie:
    def __init__(self, titulo='Defecto', NumeroTem=3, Entregado=False, genero='Base',creador='Ninguno'):
        self.titulo=titulo
        self.NumeroTem=NumeroTem
        self.Entregado=Entregado
        self.genero=genero
        self.creador=creador

    def getTitulo(self):
        return self.titulo
    def getNumeroTem(self):
        return self.NumeroTem
    def getGenero(self):
        return self.genero
    def getCreador(self):
        return self.creador

    def setTitulo(self,titulo):
        self.titulo=titulo
    def setNumeroTem(self,NumeroTem):
        self.NumeroTem=NumeroTem
    def setGenero(self,genero):
        self.genero=genero
    def setCreador(self,creador):
        self.creador=creador

    def entregar(self):
        self.Entregado = True

    def devolver(self):
        self.Entregado = False

    def entregado(self):
        if(self.Entregado==True):
            entregar= 'SI'
        else :
            entregar = 'NO'
        return entregar

    def isEntregado(self):
        if self.Entregado == True:
            return True
        else:
            return False

    def toString(self):
        print('')
        print('Titulo: ' + self.titulo)
        print('Temporada Numero: ' + str(self.NumeroTem))
        print('Entregado: ' + self.entregado())
        print('Genero: ' + self.genero)
        print('Creador:' +self.creador)
        print('')