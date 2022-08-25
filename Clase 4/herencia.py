from turtle import Vec2D


class Vehiculo:
    def __init__(self, marca):
        self.llantas = None
        self.motor = None
        self.marca = marca
        self.modelo = None
    
class Auto(Vehiculo):
    def __init__(self, marca, llantas):
        self.marca = marca
        self.llantas = llantas



class  Moto(Vehiculo):
    def __init__(self, marca="italika"):
        self.marca = marca

class Cuatrimoto(Moto):
    def __init__(self, marca):
        super().__init__(marca)


tsuru = Auto('nissan')
mortalika = Moto('italika')

print(tsuru.marca)
print(tsuru.llantas)

print(mortalika.marca)

print(mortalika.llantas)