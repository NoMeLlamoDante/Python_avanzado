
from operator import truediv


class Carro:
    def __init__(self, pasajeros, asientos, puertas, combustible, modelo):
        self.motor = 1
        self.llantas = 4
        self.pasajeros = pasajeros
        self.volante = 1
        self.asientos = asientos
        self.puertas = puertas
        self.parabrisas = 1
        self.combustible = combustible
        self.frenos = 4
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0.0 #Km/h
        # luces = 4
        # llaves
        # cinturon
        # bateria
        # marca = None
        # modelo = None

    def __str__(self):
        return self.modelo

    def encender(self):
        if self.combustible > 0:
            self.encendido = True
            self.calcular_combustible()
            print("Encendido... runnnnnn")
    
    def apagar(self):
        if(self.encendido):
            self.encendido = False
            print("Apagado...")

    def avanzar(self, direccion):
        if(self.encendido):
            self.calcular_combustible()
            print(f"Avanzando hacia {direccion}")
    
    def detener(self):
        if self.encendido:
            self.calcular_combustible()
            print("Detenido")

    def calcular_combustible(self):
        self.combustible-=1
        if self.combustible == 0:
            self.apagar();
    # checar luces

vocho = Carro(5,3,2,2.0, "vochito")
tsuru = Carro(pasajeros=5,asientos=3,puertas=4,combustible=10.0,modelo = "tsuru")

print(vocho)
print(tsuru)
vocho.encender()
vocho.avanzar("Frente")
vocho.detener()
vocho.apagar()
print(vocho.combustible);