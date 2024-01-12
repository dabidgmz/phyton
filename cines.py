from arreglo import Arreglo
from salas import Sala
from funciones import Funcione
class Cine(Arreglo):
    def __init__(self, nombre=None, colonia=None, numero=None, direccion=None, empresa=None):
        super().__init__()
        self.nombre = nombre
        self.colonia = colonia
        self.numero = numero
        self.direccion = direccion
        self.empresa = empresa
        self.salas = Sala()

    def __str__(self):
        cine_info = f"Cine: {self.nombre}, Colonia: {self.colonia}, Numero: {self.numero}, Direccion: {self.direccion}, Empresa: {self.empresa}"
        salas_info = "\n".join([str(sala) for sala in self.mostrar()])
        return cine_info + "\n" + salas_info


if __name__ == "__main__":
    cine = Cine("CineCity", "Downtown", 1, "123 Main St", "CineCorp")
    sala1 = Sala("Sala 1", 100, "Digital", "2D", "Normal")
    sala1.agregar_funcion(Funcione("Pelicula 1", "18:00", "Director 1", "Español", "120 mins"))
    sala2 = Sala("Sala 2", 80, "Digital", "3D", "VIP")
    sala2.agregar_funcion(Funcione("Pelicula 2", "20:30", "Director 2", "Inglés", "150 mins"))
    cine.agregar(sala1)
    cine.agregar(sala2)
    print(cine)