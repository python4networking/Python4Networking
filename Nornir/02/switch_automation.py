from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from datetime import datetime
import os

# Carrega as configurações de inventario
nr = InitNornir(config_file="config.yaml")

# Carrega dados dos Switches via arquivo yaml
def carrega_info_switches(task):
    switches_data = task.run(name="Carrega dados especificos dos Switches", task=load_yaml, file=f"./host_vars/{task.host}.yaml")
    task.host["info_switches"] = switches_data.result

# Gera templates de configuração    
def gera_templates(task):
    template_data = "access_switch.j2" if not task.host["info_switches"]["multilayer"] else "core_switch.j2"
    data = task.run(name="Gera template Jinja2", task=template_file, template=template_data, path="./templates")
    task.host["template_configs"] = data.result

# Conecta os dispositivos e envia templates de configuração por dispositivo
def envia_cfgs_cmds(task): 
    config_lines = task.host["template_configs"].splitlines()
    result_1 = task.run(name="Envia configuração via Netmiko", task=netmiko_send_config, config_commands=config_lines)
    task.host["resposta_netmiko"] = result_1.result
    task.host["comandos_enviados"] = config_lines
    
    cmds_list = ["show vlan brief", "\n", "show ip int brief"] 
    temp_list = []
    for cmd in cmds_list:
        result_2 = task.run(name="Coleta dados via show comandos", task=netmiko_send_command, command_string=cmd)
        temp_list.append(result_2.result)
    task.host["cmds_show"] = temp_list

# Gera logs das configurações aplicadas e geradas
def gera_log(task):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{task.host.name}_{timestamp}.log")

    with open(log_file, "w") as f:
        f.write(f"********** RELATÓRIO DE CONFIGURAÇÃO DOS SWITCH |{task.host.name}| ************\n")
        f.write(f"Data/Hora: {datetime.now()}\n")
        f.write(f"\n----------------------------- TEMPLATE APLICADO -----------------------------\n")
        f.write(task.host["template_configs"])
        f.write(f"\n\n----------------- COMANDOS ENVIADOS PARA O DISPOSITIVO --------------------\n")
        for cmd in task.host["comandos_enviados"]:
            f.write(cmd + "\n")
        f.write(f"\n-------------------------- RESPOSTA DO DISPOSITIVO --------------------------\n")
        f.write(task.host["resposta_netmiko"])
        f.write("\n")
        f.write(f"\n------------------------- VALIDAÇÃ0 NOS DISPOSITIVOS ------------------------\n")
        for cmd_show in task.host["cmds_show"]:
            f.write(cmd_show + "\n")
        f.write("\n\n************************* FIM DO RELATÓRIO *********************************\n")

def main():
    result_switches = nr.run(task=carrega_info_switches)
    result_template = nr.run(task=gera_templates)
    result_cmds = nr.run(task=envia_cfgs_cmds)
    nr.run(task=gera_log)
    print_result(result_switches)
    print_result(result_template)
    print_result(result_cmds)

if __name__ == "__main__":
    main()