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
