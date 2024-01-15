from arreglo import Arreglo
from salas import Sala
from funciones import Funcione
import json

class Cine(Arreglo):
    def __init__(self, nombre=None, colonia=None, numero=None, direccion=None, empresa=None):
        super().__init__()
        self.nombre = nombre
        self.colonia = colonia
        self.numero = numero
        self.direccion = direccion
        self.empresa = empresa
        self.salas = Arreglo()

    def agregar_sala(self, sala):
        self.salas.agregar(sala)

    def to_dict(self):
        cine_dict = {k: v.a_diccionario() if k == 'salas' else v for k, v in vars(self).items()}
        cine_dict['salas'] = self.salas.a_diccionario()
        return cine_dict

    def __str__(self):
        cine_info = f"Cine: {self.nombre}, Colonia: {self.colonia}, Numero: {self.numero}, Direccion: {self.direccion}, Empresa: {self.empresa}"
        salas_info = "\n".join([str(sala) for sala in self.salas.mostrar()])
        return cine_info + "\n" + salas_info

if __name__ == "__main__":
    cine = Cine("CineCity", "Downtown", 1, "123 Main St", "CineCorp")
    sala1 = Sala("Sala 1", 100, "Digital", "2D", "Normal")
    sala1.agregar_funcion(Funcione("Pelicula 1", "18:00", "Director 1", "Español", "120 mins"))
    sala2 = Sala("Sala 2", 80, "Digital", "3D", "VIP")
    sala2.agregar_funcion(Funcione("Pelicula 2", "20:30", "Director 2", "Inglés", "150 mins"))
    cine.agregar_sala(sala1)
    cine.agregar_sala(sala2)

    diccionario_cine = cine.to_dict()

    with open('txt.json', 'w') as archivo:
        json.dump(diccionario_cine, archivo, indent=4)

    print(diccionario_cine)