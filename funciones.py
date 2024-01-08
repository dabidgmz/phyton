class Funcione:
    def __init__(self, nombre, hora, director, idioma, duracion):
        self.nombre = nombre
        self.hora = hora
        self.director = director
        self.idioma = idioma
        self.duracion = duracion
        self.funciones = []  

    def __str__(self):
        return f"Funciones: Nombre={self.nombre}, Hora={self.hora}, Director={self.director}, Idioma={self.idioma}, Duracion={self.duracion}"

    def agregar_funcion(self, funcion):
        self.funciones.append(funcion)