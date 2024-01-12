from cines import Cine


class CRUDCine:
    def __init__(self):
        self.lista_cines = []

    def agregar_cine(self, nombre, colonia, numero, direccion, empresa):
        cine = Cine(nombre, colonia, numero, direccion, empresa)
        self.lista_cines.append(cine)
        return cine

    def mostrar_cines(self):
        return self.lista_cines

    def actualizar_cine(self, cine, nuevo_nombre, nueva_colonia, nuevo_numero, nueva_direccion, nueva_empresa):
        cine.nombre = nuevo_nombre
        cine.colonia = nueva_colonia
        cine.numero = nuevo_numero
        cine.direccion = nueva_direccion
        cine.empresa = nueva_empresa
        print("Se actualizó la información del cine con éxito.")

    def eliminar_cine(self, cine):
        self.lista_cines.remove(cine)
        print("Se eliminó el cine.")