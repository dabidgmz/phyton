from salas import Sala
from funciones import Funcione

class CRUDSala:
    def __init__(self):
        pass

    def agregar_sala(self, nombre, capacidad, sistema_digital, tp_pantalla, tp_sala):
        sala = Sala(nombre, capacidad, sistema_digital, tp_pantalla, tp_sala)
        return sala

    def mostrar_salas_en_cine(self, cine):
        return cine.salas

    def agregar_funcion_en_sala(self, sala, funcion):
        sala.agregar_funcion(funcion)

    def mostrar_funciones_en_sala(self, sala):
        return sala.funciones

    def actualizar_funcion_en_sala(self, sala, indice_funcion, nueva_funcion):
        if 0 <= indice_funcion < len(sala.funciones):
            sala.funciones[indice_funcion] = nueva_funcion
            print("Se actualizó la función en la sala con éxito.")
        else:
            print("Índice de función no válido.")

    def eliminar_funcion_en_sala(self, sala, indice_funcion):
        if 0 <= indice_funcion < len(sala.funciones):
            del sala.funciones[indice_funcion]
            print("Se eliminó la función de la sala.")
        else:
            print("Índice de función no válido.")