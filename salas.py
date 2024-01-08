from funciones import Funcione

class Sala:
    def __init__(self, nombre, capacidad, sistema_digital, tp_pantalla, tp_sala):
        self.nombre = nombre
        self.capacidad = capacidad
        self.sistema_digital = sistema_digital
        self.tp_pantalla = tp_pantalla
        self.tp_sala = tp_sala
        self.funciones = []

    def agregar_funcion(self, funcion):
        self.funciones.append(funcion)

    def __str__(self):
        sala_info = f"Salas: Nombre={self.nombre}, Capacidad: {self.capacidad}, Sistema Digital: {self.sistema_digital}, Tipo Pantalla: {self.tp_pantalla}, Tipo Sala: {self.tp_sala}"
        funciones_info = "\n".join([str(funcion) for funcion in self.funciones])
        return sala_info + "\n" + funciones_info

if __name__ == "__main__":
    sala1 = Sala("Sala 1", 100, "Digital", "Pantalla tipo A", "Sala VIP")
    sala2 = Sala("Sala 2", 150, "Análogo", "Pantalla tipo B", "Sala Estándar")
    funcion1_sala1 = Funcione("dora", "17:00", "drake", "español", "180")
    funcion2_sala1 = Funcione("peliculaX", "20:00", "directorX", "inglés", "150")
    funcion1_sala2 = Funcione("aventura", "18:30", "directorY", "español", "120")
    sala1.funciones.append(funcion1_sala1)
    sala1.funciones.append(funcion2_sala1)
    sala2.funciones.append(funcion1_sala2)

    print(sala1)
    print(sala2)