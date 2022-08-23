import requests

respuesta = requests.get("https://c2c6-187-135-193-189.ngrok.io/multiplayer/play/")
# r = requests.post('https://c2c6-187-135-193-189.ngrok.io/multiplayer/play/', data={'key': 'value'})

print(respuesta)
print(respuesta.status_code)
print(respuesta.text)
