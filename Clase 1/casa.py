class Casa:
    def __init__(self):
        self.es_grande = False
        self.puerta = 1
        self.ventana = 1
        self.escalera = 1
        self.paredes = 4
        self.color = "blanco"
        self.techo = 1

        self.valor = 1

        self.bathroom = 1
        self.kitchen = 1
        self.room = 1
        self.living = 1

    def turn_on_AC(self):
        print("ok, aire acondicionado está encendido")

    def turn_on_light(self):
        print("luz de entrada encendida")

    def use_bathroom(self):
        print("poop")
    
    def make_dinner(self):
        print("food")

casita = Casa()

print(casita.puerta)
casita.encender_ac()