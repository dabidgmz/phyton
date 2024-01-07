from salas import Sala

class Cine:
    def __init__(self, nombre, colonia, numero, direccion, empresa):
        self.nombre = nombre
        self.colonia = colonia
        self.numero = numero
        self.direccion = direccion
        self.empresa = empresa
        self.salas = []

    def __str__(self):
        return f"Cine: {self.nombre}, Colonia: {self.colonia}, Numero: {self.numero}, Direccion: {self.direccion}, Empresa: {self.empresa}"

if __name__ == "__main__":
    Cine1 = Cine("cinecity", "centro", "60", "aves", "cinemex")
    #print(Cine1)
    #print("Nombre:", Cine1.nombre)
    #print("Colonia:", Cine1.colonia)
    #print("Numero:", Cine1.numero)
    #print("Direccion:", Cine1.direccion)
    #print("Empresa:", Cine1.empresa)
    #sala1 = Sala("Sala 1", 100, "Digital", "Pantalla tipo A", "Sala VIP")
    #sala2 = Sala("Sala 2", 150, "Análogo", "Pantalla tipo B", "Sala Estándar")
    #Cine1.salas.append(sala1)
    #Cine1.salas.append(sala2)
    #for sala in Cine1.salas:
    #   print(f"Sala: {sala.nombre}, Capacidad: {sala.capacidad}, Sistema Digital: {sala.sistema_digital}, Tipo de Pantalla: {sala.tp_pantalla}, Tipo de Sala: {sala.tp_sala}")