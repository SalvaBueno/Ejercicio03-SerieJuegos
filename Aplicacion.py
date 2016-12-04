from Serie import Serie
from Videojuego import Videojuego

class Aplicacion():

    def exe(self):

        listaSerie = []
        listaVideo = []

        listaSerie.append(Serie('Sobrenatural',11,False,'Suspense/Terror','Eric Kripke'))
        listaSerie.append(Serie('The Big Bang Theory',10,False,'Comedia','Chuck Lorre Bill Prady'))
        listaSerie.append(Serie('Agents of Shield',4,False,'Accion/Ficcion/Drama','Joss Whendon'))
        listaSerie.append(Serie('Mr.Robot',2,False,'Crimen Drama','Sam Esmail'))
        listaSerie.append(Serie('Ash vs Evil dead',2,False,'Comedia/Terror','Sam Raimi'))

        listaVideo.append(Videojuego('League of Legends',10000,False,'Videojuego multijugador','Riot Games'))
        listaVideo.append(Videojuego('OverWatch',5000,False,'VideoJuego multijugador','Blizzard'))
        listaVideo.append(Videojuego('World of Warcraft',9999,False,'Multijugador masivo','Blizzard'))
        listaVideo.append(Videojuego('Hearthstone',5000,False,'Videojuego Multijugador','Blizzard'))
        listaVideo.append(Videojuego('Heroes of the Storm',4000,False,'Videojuego multijugador','Blizzard'))

        listaVideo[2].entregar()
        listaSerie[1].entregar()
        listaSerie[4].entregar()
        listaVideo[3].entregar()

        videoEntregado=0
        serieEntregada=0

        for i in listaVideo:
            if(i.isEntregado()):
                videoEntregado+=1
                i.devolver()

        for i in listaSerie:
            if(i.isEntregado()) :
                serieEntregada+=1
                i.devolver()

        print("VideoJuegos Entregados: "+str(videoEntregado))
        print("Series Entregadas: "+ str(serieEntregada))
        print('')

        max=0
        for i in listaSerie:
            if(max < i.getNumeroTem()) :
                max = i.getNumeroTem()
                nomSmax= i.getTitulo()

        for i in listaVideo:
            if(max < i.getHorasEsti()) :
                max = i.getHorasEsti()
                nomVmax= i.getTitulo()

        print("La serie con mas temporadas es: "+nomSmax)
        print("El videojuego con mas horas estimadas es :" +nomVmax)
        print('')



run = Aplicacion()
run.exe()