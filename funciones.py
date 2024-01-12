from arreglo import Arreglo
class Funcione:
    def __init__(self, nombre, hora, director, idioma, duracion):
        self.nombre = nombre
        self.hora = hora
        self.director = director
        self.idioma = idioma
        self.duracion = duracion
        self.funciones = Arreglo()

    def agregar_funcion(self, funcion):
        self.funciones.agregar(funcion)

    def mostrar_funciones(self):
        return self.funciones.mostrar()

    def ver_funcion(self, indice):
        return self.funciones.ver(indice)

    def modificar_funcion(self, indice, nueva_funcion):
        return self.funciones.modificar(indice, nueva_funcion)

    def eliminar_funcion(self, indice):
        return self.funciones.eliminar(indice)

    def __str__(self):
        return f"Funciones: Nombre={self.nombre}, Hora={self.hora}, Director={self.director}, Idioma={self.idioma}, Duracion={self.duracion}"
