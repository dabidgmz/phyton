from arreglo import Arreglo

class Funcione(Arreglo):
    def __init__(self,nombre=None, hora=None, director=None, idioma=None, duracion=None):
        super().__init__()
        self.nombre = nombre
        self.hora = hora
        self.director = director
        self.idioma = idioma
        self.duracion = duracion

    def __str__(self):
        if not self.elementos:
            return f"Funciones: Nombre={self.nombre}, Hora={self.hora}, Director={self.director}, Idioma={self.idioma}, Duracion={self.duracion}\nEste es un arreglo de funciones vacío."
        else:
            return f"Este es un arreglo de funciones y sus elementos: {self.elementos}"