from urllib import response
import requests

respuesta = requests.get("http://127.0.0.1:8000/multiplayer/play/")

print(respuesta)

print(respuesta.status_code)

#print(respuesta.text)