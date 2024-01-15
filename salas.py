from funciones import Funcione

class Sala:
    def __init__(self, nombre=None, capacidad=None, sistema_digital=None, tp_pantalla=None, tp_sala=None):
        self.nombre = nombre
        self.capacidad = capacidad
        self.sistema_digital = sistema_digital
        self.tp_pantalla = tp_pantalla
        self.tp_sala = tp_sala
        self.funciones = Funcione()

    def agregar_funcion(self, funcion):
        self.funciones.agregar(funcion)

    def __str__(self):
        sala_info = f"Salas: Nombre={self.nombre}, Capacidad: {self.capacidad}, Sistema Digital: {self.sistema_digital}, Tipo Pantalla: {self.tp_pantalla}, Tipo Sala: {self.tp_sala}"
        funciones_info = "\n".join([str(funcion) for funcion in self.funciones.mostrar()])
        return sala_info + "\n" + funciones_info

    def a_diccionario(self):
        return {"nombre": self.nombre, "capacidad": self.capacidad, "sistema_digital": self.sistema_digital, "tp_pantalla": self.tp_pantalla, "tp_sala": self.tp_sala, "funciones": self.funciones.a_diccionario()}