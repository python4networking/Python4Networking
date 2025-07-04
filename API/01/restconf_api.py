import requests
import urllib3
from rich import print as rprint

# Desabilita warnings de certificado inválido 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Informações do Host
HOST = "NOME DO HOST"
USERNAME = "SEU_USERNAME"
PASSWORD = "SUA_SENHA"

URL= f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"


headers = {
    "Accept" : "application/yang-data+json",
    "Content-Type" : "application/yang-data+json"
    }

resposta = requests.get(URL, auth=(USERNAME, PASSWORD), headers=headers, verify=False).json()

intfs = resposta["ietf-interfaces:interfaces"]["interface"]
rprint(intfs)

for intf in intfs:
    if (len(intf["ietf-ip:ipv4"])) > 0:        
        print(f"Interface: {intf["name"]}")
        print(f"IP: {intf["ietf-ip:ipv4"]["address"][0]["ip"]}")
        print(f"Mascara: {intf["ietf-ip:ipv4"]["address"][0]["netmask"]}")
        print("-" * 120)


