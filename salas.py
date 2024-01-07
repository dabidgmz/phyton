class Sala:
    def __init__(self, nombre, capacidad, sistema_digital, tp_pantalla, tp_sala):
        self.nombre = nombre
        self.capacidad = capacidad
        self.sistema_digital = sistema_digital
        self.tp_pantalla = tp_pantalla
        self.tp_sala = tp_sala

    def __str__(self):
        return f"Salas: Nombre={self.nombre}, Capacidad: {self.capacidad}, Sistema Digital: {self.sistema_digital}, Tipo Pantalla: {self.tp_pantalla}, Tipo Sala: {self.tp_sala}"

if __name__ == "__main__":
    Salas1 = Sala("A1", "100", "Dolby", "3D", "Amplia")
    #print(Salas1)
    #print("Nombre:", Salas1.nombre)
    #print("Capacidad:", Salas1.capacidad)
    #print("Sistema Digital:", Salas1.sistema_digital)
    #print("Tipo Pantalla:", Salas1.tp_pantalla)
    #print("Tipo Sala:", Salas1.tp_sala)