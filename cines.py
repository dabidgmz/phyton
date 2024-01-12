from salas import Sala
from arreglo import Arreglo

class Cine(Arreglo):
    def __init__(self, nombre, colonia, numero, direccion, empresa):
        super().__init__()  
        self.nombre = nombre
        self.colonia = colonia
        self.numero = numero
        self.direccion = direccion
        self.empresa = empresa

    def agregar_sala(self, sala):
        self.agregar(sala)

    def mostrar_salas(self):
        return self.mostrar()

    def ver_sala(self, indice):
        return self.ver(indice)

    def modificar_sala(self, indice, nueva_sala):
        return self.modificar(indice, nueva_sala)

    def eliminar_sala(self, indice):
        return self.eliminar(indice)

    def __str__(self):
        cine_info = f"Cine: {self.nombre}, Colonia: {self.colonia}, Numero: {self.numero}, Direccion: {self.direccion}, Empresa: {self.empresa}"
        salas_info = "\n".join([str(sala) for sala in self.mostrar_salas()])
        return cine_info + "\n" + salas_info