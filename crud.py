from salas import Sala
from funciones import Funcione

class CRUD:
    def __init__(self):
        pass

    def agregar(self, funcion_container, funcion):
        funcion_container.agregar_funcion(funcion)

    def ver(self, funcion_container):
        return funcion_container.funciones

    def mostrar(self, cine):
        funciones_cine = []
        for sala in cine.salas:
            funciones_cine.extend(sala.funciones)
        return funciones_cine

    def actualizar(self, funcion_container, indice_funcion, nueva_funcion):
        if 0 <= indice_funcion < len(funcion_container.funciones):
            funcion_container.funciones[indice_funcion] = nueva_funcion
            print("Se actualizó con éxito.")
        else:
            print("Índice de función no válido.")

    def eliminar(self, funcion_container, indice_funcion):
        if 0 <= indice_funcion < len(funcion_container.funciones):
            del funcion_container.funciones[indice_funcion]
            print("Se eliminó la función.")
        else:
            print("Índice de función no válido.")