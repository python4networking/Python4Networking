import os
import urllib3
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from rich import print as rprint
from datetime import datetime
from dotenv import load_dotenv

# Desabilita warnings de certificado
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Carrega variáveis do .env
load_dotenv()

def nornir_inicializacao():
    # Inicializa o Nornir com NetBox
    nr = InitNornir(config_file="./Nornir_Netbox/config.yaml")
    return nr

def bkp_dispositivos(task):
    # Função para realizar backup dos dispositivos
    if "ios" in task.host.platform:
        task.host.username = os.getenv("CISCO_USERNAME")
        task.host.password = os.getenv("CISCO_PASSWORD")
    elif "eos" in task.host.platform:
        task.host.username = os.getenv("ARISTA_USERNAME")
        task.host.password = os.getenv("ARISTA_PASSWORD")
    else:
        rprint(f"[red]❌ Grupo desconhecido para {task.host}[/red]")
        return

    data = task.run(task=napalm_get, getters=["config"])
    running_config = data.result["config"]["running"]

    directory = "./Backups"
    os.makedirs(directory, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{directory}/Bkp_{task.host.name}_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(running_config)
    rprint(f"[green]✅ Backup realizado com sucesso: {filename}[/green]")

def main():
    nr = nornir_inicializacao()
    result = nr.run(task=bkp_dispositivos)
    print_result(result)

if __name__ == "__main__":
    main()
