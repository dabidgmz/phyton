from funciones import Funcione
from salas import Sala

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
    Cine1 = Cine("cinecity", "centro", "60", "aves", "cinemex")
    sala1 = Sala("Sala1", 100, "Digital", "Pantalla tipo A", "Sala VIP")
    sala2 = Sala("Sala2", 150, "Análogo", "Pantalla tipo B", "Sala Estándar")
    funcion1_sala1 = Funcione("dora", "17:00", "drake", "español", "180")
    funcion2_sala1 = Funcione("peliculaX", "20:00", "directorX", "inglés", "150")
    funcion1_sala2 = Funcione("aventura", "18:30", "directorY", "español", "120")
    sala1.agregar_funcion(funcion1_sala1)
    sala1.agregar_funcion(funcion2_sala1)
    sala2.agregar_funcion(funcion1_sala2)
    Cine1.agregar_sala(sala1)
    Cine1.agregar_sala(sala2)
    print("\nSalas con Funciones:")
    for sala in Cine1.salas:
        print(sala)