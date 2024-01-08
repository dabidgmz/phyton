from salas import Sala
from funciones import Funcione
from crud import CRUD

class Cine:
    def __init__(self, nombre, colonia, numero, direccion, empresa):
        self.nombre = nombre
        self.colonia = colonia
        self.numero = numero
        self.direccion = direccion
        self.empresa = empresa
        self.salas = []

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def __str__(self):
        cine_info = f"Cine: {self.nombre}, Colonia: {self.colonia}, Numero: {self.numero}, Direccion: {self.direccion}, Empresa: {self.empresa}"
        salas_info = "\n".join([str(sala) for sala in self.salas])
        return cine_info + "\n" + salas_info

if __name__ == "__main__":
    Funciones1 = Funcione("nemo", "17:00", "Drake", "Español", "180")
    Sala1 = Sala("Sala 1", 100, "Digital", "Tipo A", "VIP")
    Sala1.agregar_funcion(Funciones1)

    Funciones2 = Funcione("inception", "19:30", "Nolan", "Ingles", "150")
    Sala1.agregar_funcion(Funciones2)

    Cine1 = Cine("CineCity", "Central", "123", "Main St", "CineCorp")
    Cine1.agregar_sala(Sala1)
    
    print("Initial State:")
    print(Cine1)

    cruds = CRUD()

    nueva_funcion = Funcione("Spiderman", "21:00", "Sony", "Español", "120")
    cruds.agregar_funcion(Sala1, nueva_funcion)
    nueva_funcion2 = Funcione("Black Widow", "20:00", "Marvel", "Ingles", "130")
    cruds.agregar_funcion(Sala1, nueva_funcion2)
    nueva_funcion3 = Funcione("The Matrix", "22:30", "Wachowski", "Ingles", "140")
    cruds.agregar_funcion(Sala1, nueva_funcion3)
    nueva_funcion_modificada = Funcione("Spiderman 2", "21:30", "Sony", "Español", "125")
    cruds.actualizar_funcion(Sala1, 0, nueva_funcion_modificada)
    cruds.eliminar_funcion(Sala1, 1)
    print("\nUpdated State:")
    print(Cine1)
