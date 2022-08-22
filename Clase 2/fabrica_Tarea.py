"""
Modificar la clase Carro para que sea genérica
La fábrica podrá crear diferentes modelos de carros ej: Tsuru, Versa, Sentra
Cada modelo de carro debe tener una característica única
No repetir Numeros de serie
"""
import random


class Carro:
    def __init__(self,
                motorizacion, 
                llantas, 
                pasajeros, 
                volante, 
                asientos, 
                puertas, 
                parabrisas,  
                combustible,
                transmision, 
                tipo,
                frenos, 
                modelo, 
                color = None,
                vin = None):
        self.motorizacion = motorizacion
        self.llantas = llantas
        self.pasajeros = pasajeros
        self.volante = volante
        self.asientos = asientos
        self.puertas = puertas
        self.parabrisas = parabrisas
        self.combustible = combustible
        self.transmision = transmision
        self.tipo = tipo
        self.frenos = frenos
        self.modelo = modelo
        self.color = color
        #self.encendido = False
        #self.velocidad = 0.0 #Km/h
        self.vin = vin
        # color
        # caracteristicas

    def __str__(self):
        return f"modelo: {self.modelo}, Transmision: {self.transmision} Color: {self.color}, serial: {self.vin}"

    def randomColor(self):
        colores = ['Azul','Negro', 'Blanco', 'Rojo', 'Gris', 'Verde']
        self.color = random.choice(colores)


class Fabrica():
    def __init__(self):
        self.almacen = []
        self.serial = 1

    def fabricar(self, plano_carro, cantidad, color=None):
        for i in range(cantidad):
            #carro = self.plano_carro(
            #            pasajeros = 4, 
            #            asientos =  3, 
            #            puertas = 4, 
            #            combustible = 2, 
            #            modelo = "Tsuru",
            #            vin = self.serial)
            #Crear el carro de acuerdo al plano
            carro = Carro(
                motorizacion= plano_carro.motorizacion,
                llantas= plano_carro.llantas,
                pasajeros= plano_carro.pasajeros,
                volante= plano_carro.volante,
                asientos= plano_carro.asientos,
                puertas = plano_carro.puertas,
                parabrisas= plano_carro.parabrisas,
                combustible= plano_carro.combustible,
                transmision= plano_carro.transmision,
                tipo= plano_carro.tipo,
                frenos= plano_carro.frenos,
                modelo= plano_carro.modelo,
                vin= self.serial)
            #elegir Color
            if color == None:
                carro.randomColor()
            else:
                carro.color = color
            
            self.almacen.append(carro)
            #self.almacen[i].vin = self.serial
            self.serial+=1

#Iniciar Fábrica 
nissan = Fabrica()
#descripción de carro
march_TA = Carro(motorizacion= 2.4, llantas= 4, pasajeros= 5,volante= 1,asientos= 3,puertas= 4,parabrisas= 2,
            combustible= "gasolina",transmision= "estandar",tipo= "hatchback",frenos= 4, modelo= "march")

versa = Carro(motorizacion= 2.4, llantas= 4, pasajeros= 5,volante= 1,asientos= 3,puertas= 4,parabrisas= 2,
            combustible= "gasolina",transmision= "automatica",tipo= "sedan",frenos= 4, modelo= "versa")

march_TS = Carro(motorizacion= 2.4, llantas= 4, pasajeros= 5,volante= 1,asientos= 3,puertas= 4,parabrisas= 2,
            combustible= "gasolina",transmision= "automatica",tipo= "hatchback",frenos= 4, modelo= "march")
#print(nissan.almacen)
nissan.fabricar(march_TA,3)
nissan.fabricar(versa,5)
nissan.fabricar(march_TS,2)


#print(nissan.almacen)

for carro in nissan.almacen:
    print(carro)


#poner numero de serie al carro