from funciones import Funcione
from salas import Sala
from cines import Cine
from arreglo import Arreglo

if __name__ == "__main__":
    cine = Cine("CineCity", "Downtown", 1, "123 Main St", "CineCorp")
    sala1 = Sala("Sala 1", 100, "Digital", "2D", "Normal")
    sala1.agregar_funcion(Funcione("Pelicula 1", "18:00", "Director 1", "Español", "120 mins"))
    sala2 = Sala("Sala 2", 80, "Digital", "3D", "VIP")
    sala2.agregar_funcion(Funcione("Pelicula 2", "20:30", "Director 2", "Inglés", "150 mins"))
    cine.agregar_sala(sala1)
    cine.agregar_sala(sala2)
    print(cine)
