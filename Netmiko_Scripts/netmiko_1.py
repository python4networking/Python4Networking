"""
 OBJETIVOS:
    1. Coletar running config dos dispositivos Cisco, Juniper e via Nornir-napal e salvar config em arquivos txt com data/hora.
    2. Configurar agendamento de tarefas no crontab Linux 
"""

##--Tarefas--##
#--------------------------------------------------------
# 1.1 Inicialização do Nornir
# (OK)
#--------------------------------------------------------
# 1.2 Definir função (task)
#   1.2.1 - Obter configuração
# (OK)
#   1.2.2 - Criar diretório
# (OK)
#   1.2.3 - Obter nome do group
# (OK)
#   1.2.4 - Definir timestamp
# (OK)
#   1.2.4 - Criar arquivo e salvar
# (OK)
#--------------------------------------------------------
# 2. Configurar agendamento de tarefas no crontab Linux 
#--------------------------------------------------------

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from rich import print as rprint
import os
from datetime import datetime

# 1.1 Inicialização do Nornir
nr = InitNornir(config_file="INSERIR PATH/config.yaml")

# 1.2 Definir função (task)
def bkp_devices(task):

    # 1.2.3 - Obter nome do group
    if task.host.groups[0].name:
        group_name = task.host.groups[0].name
    else:
        group_name = "default" 

    #1.2.1 - Obter configuração
    data = task.run(task=napalm_get, getters=["config"])
    running_config = data.result["config"]["running"]

    # 1.2.2 - Criar diretório
    directory = f"INSERIR PATH/Scripts/Backups/{group_name}"
    os.makedirs(directory, exist_ok=True)

    # 1.2.4 - Definir timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{directory}/Bkp_{task.host.name}_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(running_config)
    
    rprint("[green]✅ Backup realizado com sucesso: {filename}[/green]")


result = nr.run(task=bkp_devices)
print_result(result)
