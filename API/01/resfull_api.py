import requests
from rich import print as rprint

# Localizar Latitude e Longitude em latlong.net 
LAT = -23.550520
LON = -46.633308
API_KEY = "SUA_API_KEY"

# URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

# resposta = requests.get(URL).json()
# rprint(resposta["name"])


resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
rprint(resposta.json())


