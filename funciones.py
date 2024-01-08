class Funcione:
    def __init__(self, nombre, hora, director, idioma, duracion):
        self.nombre = nombre
        self.hora = hora
        self.director = director
        self.idioma = idioma
        self.duracion = duracion

    def __str__(self):
        return f"Funciones: Nombre={self.nombre}, Hora={self.hora}, Director={self.director}, Idioma={self.idioma}, Duracion={self.duracion}"

if __name__ == "__main__":
    Funciones1 = Funcione("dora", "17:00", "drake", "español", "180")
    print(Funciones1)
    print("Nombre:", Funciones1.nombre)
    print("Hora:", Funciones1.hora)
    print("Director:", Funciones1.director)
    print("Idioma:", Funciones1.idioma)
    print("Duracion:", Funciones1.duracion)