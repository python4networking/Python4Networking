
#!/usr/bin/env python3
"""
Python4Networking - Trilha Python para Profissionais de Rede
Episódio 4: Funções main(), menu(), coleta_informacaoes() 
Episódio 5: Correções/Refatorar e função configura_dispositivos()

## Objetivo (Ep. 5) ##
- Mostrar como dividir um script real em funções pequenas e reaproveitáveis.

## O que o script precisa fazer hoje (Ep4) ##
|Funções principais|
    a. Coletar informações (show version / show ip int brief / show ip route)
        a1. Importar Inventário e acessar inventario
        a2. Criar função coleta_informacoes()
            a2.1 Conectar dispositivos via Netmiko de maneira simples
        a4. Criar função main() e testa
        a5. Criar menu (1 e 0)
    b. Criar funcao Configuração de dispositivos
        b1. Criar funcao separada para conectar dispositivos
        b2. Criar funcao configura_dispositivos(), menu_config(), renderiza_template(), aquivo j2 
    c. Criar funcao Localizar MAC na rede 
    d. Criar Backup de configurações

|Refatorar|
    a. try/else
    b. if/elif
    
"""
from devices_inventory import DEVICES
from rich import print as rprint
from netmiko import ConnectHandler
import os
from jinja2 import Template

APP_NAME = "NetAutomation CLI Toolkit"
APP_VERSION = "1.1 (Ep5)"
LINE = "=" * 180
DIR_TEMPLATE = "./Trilha Python/templates"
CAMINHO_TEMPLATE = os.path.join(DIR_TEMPLATE, "vlan.j2")

def menu():
    os.system('clear')
    rprint("\n" + LINE)
    rprint(f"[green]{APP_NAME}  |  {APP_VERSION}[/green]")
    rprint(LINE)
    print("\nSelecione uma opção:")
    print("  1) Coleta de informações (Cisco/Arista)")
    print("  2) Localizar MAC address na rede [EPx]")
    print("  3) Configuração de dispositivos  [EP5]")
    print("  4) Backup de configurações       [EPx]")
    print("  0) Sair")

def menu_config():
    os.system('clear')
    rprint("\n" + LINE)
    rprint(f"{APP_NAME}  |  {APP_VERSION}")
    rprint(LINE)
    print("\nSelecione uma opção:")
    print("  1) Configuração de Switch")
    print("  0) Sair")
    opcao_config = input()
    if opcao_config == "0":
        menu()
    else:
        configura_dispositivos()
        pause()
        

def pause():
    input("ENTER PARA CONTINUAR....")
    os.system('clear')


def conecta_dispositivos(device):
    conn = ConnectHandler(
        device_type=device['device_type'],
        host=device['host'],
        username = device['username'],
        password = device['password'],
        )   
    return conn 


def coleta_informacoes():
    lista_cmds_cisco = ['show version', 'show ip int brief', 'show ip route']
    lista_cmds_arista = ['show version']
    for device in DEVICES:
        try:
            print(LINE)
            rprint(f'[green]DEVICE: {device['host']} | Versao OS: {device['device_type']} | NAME: {device['device_name']} | FABRICANTE: {device['vendor']}[/green]')
            print(LINE)
            conn = conecta_dispositivos(device)
            if device['device_type'] == "cisco_ios":
                for cmd in lista_cmds_cisco:
                    resultado_cmds = conn.send_command(cmd)
                    print(resultado_cmds)
            elif device['device_type'] == "arista_eos":
                for cmd in lista_cmds_arista:
                    resultado_cmds = conn.send_command(cmd)
                    print(resultado_cmds)
            conn.disconnect()  
        except Exception as e:
            rprint(f"[red]Não foi possivel conectar ao dispositivo ❌[/red]")


def renderiza_template(caminho_template, info_configs):
    with open(CAMINHO_TEMPLATE, 'r') as arquivo:
        config = arquivo.read()
        config_renderizada = Template(config).render(**info_configs)
        rprint("Renderizando...")
        comandos = []
        for linha in config_renderizada.splitlines():
            if linha:
                comandos.append(linha)
        print("Configs renderizada")
        print("Lista de comandos: ", comandos)
        return comandos


def verifica_ip(ip):
    for device in DEVICES:
        if ip == device['host']:
            return True
    return False


def configura_dispositivos():
    ip = input('Entre do IP Switch: ')
    if verifica_ip(ip):
        vlan_id = input('Entre do VLAN ID Switch: ')
        vlan_nome = input('Entre com nome da VLAN: ')
        interface = input('Entre com o nome da interface (Ex: e0/2, ...) ')
        info_configs = {'vlan_id': vlan_id, 'vlan_nome' : vlan_nome ,'interface': interface}

        comandos = renderiza_template(CAMINHO_TEMPLATE,info_configs)
    
        for device in DEVICES:
            if ip == device['host']:
                try:
                    print(LINE)
                    rprint(f'[green]DEVICE: {device['host']} | Versao OS: {device['device_type']} | NAME: {device['device_name']} | FABRICANTE: {device['vendor']}[/green]')
                    print(LINE)
                    conn = conecta_dispositivos(device)
                    if device['device_type'] == "cisco_ios":
                        resultado_cmds = conn.send_config_set(comandos)
                        print(resultado_cmds)
                    elif device['device_type'] == "arista_eos":
                        resultado_cmds = conn.send_config_set(comandos)
                        print(resultado_cmds)
                    conn.disconnect()  
                except Exception as e:
                    rprint("[red]Não foi possivel conectar ao dispositivo ❌[/red]")
    else:
        rprint(f'[red]IP digitado não existe no inventário![/red]!!')


def main():
    os.system('clear')
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            coleta_informacoes()
            pause()
        elif opcao == "3":
            menu_config()
        elif opcao == "0":
            break
        else:
            print()
            rprint("[red]Opção não valida no menu!!![/red]")
            print()
            pause()

if __name__ == "__main__":
    main()

