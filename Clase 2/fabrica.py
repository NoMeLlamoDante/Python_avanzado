"""
Modificar la clase Carro para que sea genérica
La fábrica podrá crear diferentes modelos de carros ej: Tsuru, Versa, Sentra
Cada modelo de carro debe tener una característica única
No repetir Numeros de serie
"""

class Carro:
    def __init__(self, pasajeros, asientos, puertas, combustible, modelo, vin):
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
        self.vin = vin
        # color
        # caracteristicas


    def __str__(self):
        return self.modelo

class Fabrica():
    def __init__(self, plano_carro):
        self.plano_carro = plano_carro
        self.almacen = []
        self.serial = 1

    def fabricar(self,cantidad):
        for i in range(cantidad):
            carro = self.plano_carro(
                        pasajeros = 4, 
                        asientos =  3, 
                        puertas = 4, 
                        combustible = 2, 
                        modelo = "Tsuru",
                        vin = self.serial)
            self.serial+=1
            self.almacen.append(carro)


nissan = Fabrica(Carro)

#print(nissan.almacen)
nissan.fabricar(2)
nissan.fabricar(3)
nissan.fabricar(1)
#print(nissan.almacen)

for carro in nissan.almacen:
    print(carro, carro.vin)


#poner numero de serie al carro