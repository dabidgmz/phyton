# arreglo.py
class Arreglo:
    def __init__(self):
        self.elementos = []

    def agregar(self, instancia):
        if instancia is None:
            return False
        else:
            self.elementos.append(instancia)
            return True

    def mostrar(self):
        return self.elementos

    def ver(self, indice):
        if 0 <= indice < len(self.elementos):
            return self.elementos[indice]
        else:
            return None

    def modificar(self, indice, instancia):
        if 0 <= indice < len(self.elementos) and instancia is not None:
            self.elementos[indice] = instancia
            return True
        else:
            return False

    def eliminar(self, indice):
        if 0 <= indice < len(self.elementos):
            del self.elementos[indice]
            return True
        else:
            return False

    def a_diccionario(self):
        return {"elementos": [elemento.a_diccionario() for elemento in self.elementos]}
