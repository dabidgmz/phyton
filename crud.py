class CRUD:
    def __init__(self):
        pass

    def agregar_funcion(self, sala, funcion):
        sala.agregar_funcion(funcion)

    def actualizar_funcion(self, sala, indice_funcion, nueva_funcion):
        if 0 <= indice_funcion < len(sala.funciones):
            sala.funciones[indice_funcion] = nueva_funcion
            print("se acutalizo con exito")
        else:
            print("Índice de función no válido.")

    def eliminar_funcion(self, sala, indice_funcion):
        if 0 <= indice_funcion < len(sala.funciones):
            del sala.funciones[indice_funcion]
            print("se elimino la funcion")
        else:
            print("Índice de función no válido.")
