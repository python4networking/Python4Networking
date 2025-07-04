import requests
from rich import print as rprint

# Localizar Latitude e Longitude em latlong.net 
LAT = -23.550520
LON = -46.633308
API_KEY = "16749e0d1d2ec74c2b6c64b95dd20bdc"

# URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

# resposta = requests.get(URL).json()
# rprint(resposta["name"])


resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
rprint(resposta.json())


