from funciones import Funcione

class Sala:
    def __init__(self, nombre, capacidad, sistema_digital, tp_pantalla, tp_sala):
        self.nombre = nombre
        self.capacidad = capacidad
        self.sistema_digital = sistema_digital
        self.tp_pantalla = tp_pantalla
        self.tp_sala = tp_sala
        self.funciones = []

    def __str__(self):
        sala_info = f"Salas: Nombre={self.nombre}, Capacidad: {self.capacidad}, Sistema Digital: {self.sistema_digital}, Tipo Pantalla: {self.tp_pantalla}, Tipo Sala: {self.tp_sala}"
        funciones_info = "\n".join([str(funcion) for funcion in self.funciones])
        return sala_info + "\n" + funciones_info

    def agregar_funcion(self, funcion):
        self.funciones.append(funcion)
