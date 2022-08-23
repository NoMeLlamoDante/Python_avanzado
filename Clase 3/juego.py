import requests

#r = requests.post('https://c2c6-187-135-193-189.ngrok.io/multiplayer/play/', data={'key': 'value'})


class Carro:
    def __init__(self, piloto, modelo):
        self.piloto = piloto
        self.modelo = modelo

    def acelerar(self, opcion):
        datos = {
            'player': self.piloto,
            'key_pressed': opcion
        }
        respuesta = requests.post('https://c2c6-187-135-193-189.ngrok.io/multiplayer/play/', data=datos)
        print(f"{respuesta.status_code} {respuesta.text}")


lancer = Carro("Dante", "lancer")

while True:
    opcion = input("[1] Acelerar\n")
    lancer.acelerar(opcion)
    if opcion == '0':
        break;
