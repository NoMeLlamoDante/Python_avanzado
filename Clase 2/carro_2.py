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
        print("Apagado...")

    def avanzar(self, direccion):
        print(f"avanzando hacia {direccion}")
        self.velocidad+=1
        print(f"a una velocidad de {self.velocidad}")
    
    def detener(self):
        self.velocidad -= 1
        print("Deteniendo..")
        print(f"velocidad actual {self.velocidad}")
        if self.velocidad == 0:
            return True
        return False

    def calcular_combustible(self):
        if self.combustible == 0:
            self.apagar();
        self.combustible-=1


tsuru = Carro(pasajeros=5,asientos=3,puertas=4,combustible=10.0,modelo = "tsuru")

tsuru.encender()
while True:
    menu = """
    [1] Avanzar 
    [2] Detener
    """
    opcion = input(menu)
    if opcion == "1":
        tsuru.avanzar("Linea Recta")
    if opcion == "2":
        if tsuru.detener():
            break
    

