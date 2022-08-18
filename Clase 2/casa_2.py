class Casa:
    def __init__(self, habitantes):
        self.puerta = 1
        self.cuartos = 2
        self.techo = 1
        self.banio = 1
        self.cocina = 1
        self.ventanas = 4
        self.habitantes = habitantes

casita = Casa(2)
casita_2 = Casa(6)

print (casita.habitantes)
print (casita_2.habitantes)