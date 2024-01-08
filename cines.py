from salas import Sala
from funciones import Funcione

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
    Funciones1 = Funcione("Dora", "17:00", "Drake", "Español", "180")
    Sala1 = Sala("Sala 1", 100, "Digital", "Tipo A", "VIP")
    Sala1.agregar_funcion(Funciones1)
    Cine1 = Cine("CineCity", "Central", "123", "Main St", "CineCorp")
    Cine1.agregar_sala(Sala1)

    print(Cine1)
