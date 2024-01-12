from funciones import Funcione
from salas import Sala
from cines import Cine
from crudcinesalas import CRUDSala
from crucine import CRUDCine
from crud import CRUD

if __name__ == "__main__":
    Funciones1 = Funcione("nemo", "17:00", "Drake", "Español", "180")
    Sala1 = Sala("Sala 1", 100, "Digital", "Tipo A", "VIP")
    Sala1.agregar_funcion(Funciones1)
    Funciones2 = Funcione("inception", "19:30", "Nolan", "Ingles", "150")
    Sala1.agregar_funcion(Funciones2)
    Cine1 = CRUDCine().agregar_cine("CineCity", "Central", "123", "Main St", "CineCorp")
    Cine1.agregar_sala(Sala1)
    print("Initial State:")
    print(Cine1)
    cruds = CRUD()
    print("\nFunctions in Cine1:")
    funciones_en_cine = cruds.mostrar(Cine1)
    for funcion in funciones_en_cine:
        print(funcion)
    nueva_funcion = Funcione("Spiderman", "21:00", "Sony", "Español", "120")
    cruds.agregar(Sala1, nueva_funcion)
    nueva_funcion2 = Funcione("Black Widow", "20:00", "Marvel", "Ingles", "130")
    cruds.agregar(Sala1, nueva_funcion2)
    nueva_funcion3 = Funcione("The Matrix", "22:30", "Wachowski", "Ingles", "140")
    cruds.agregar(Sala1, nueva_funcion3)
    nueva_funcion_modificada = Funcione("Spiderman 2", "21:30", "Sony", "Español", "125")
    cruds.actualizar(Sala1, 0, nueva_funcion_modificada)
    cruds.eliminar(Sala1, 1)
    print("\nUpdated State:")
    print(Cine1)
