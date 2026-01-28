

#!/usr/bin/env python3
"""
Python4Networking - Trilha Python para Profissionais de Rede
Episódio 4: Funções main(), menu(), coleta_informacaoes() 
Episódio 5: Correções/Refatorar e função configura_dispositivos()

## Objetivo (Ep. 6) ##
- Mostrar como dividir um script real em funções pequenas e reaproveitáveis.

## O que o script precisa fazer hoje (Ep6) ##
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
        c1. Criar funcao normaliza_mac()
        c2. Criar funcao localiza_mac() 
    d. Criar Backup de configurações
        d1. Criar funcao bkp_configs()

|Melhorias|
    a. .env para credenciais
    b. Tratamento de erros/refatorar
    c. Barra de progresso Rich no backup
    d. Documentação do código
      
"""
from time import sleep
from devices_inventory import DEVICES
from rich import print as rprint
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.console import Console
from netmiko import ConnectHandler
import os
from jinja2 import Template
from dotenv import load_dotenv

load_dotenv()


console = Console()

APP_NAME = "NetAutomation CLI Toolkit"
APP_VERSION = "1.2 (Ep6)"
LINE = "=" * 180
DIR_TEMPLATE = "./Trilha Python/templates"
CAMINHO_TEMPLATE = os.path.join(DIR_TEMPLATE, "vlan.j2")


def app_info():          
    os.system('clear')
    rprint("\n" + LINE)
    rprint(f"[green]{APP_NAME}  |  {APP_VERSION}[/green]")
    rprint(LINE) 


def menu():
    print("\nSelecione uma opção:")
    print("  1) Coleta de informações (Cisco/Arista) [EP4]")
    print("  2) Localizar MAC address na rede [EP6]")
    print("  3) Configuração de dispositivos  [EP5]")
    print("  4) Backup de configurações       [EP6]")
    print("  0) Sair")


def menu_config():
    print("\nSelecione uma opção:")
    print("  1) Configuração de VLAN (Switch)")
    print("  0) Sair")
    opcao_config = input()
    if opcao_config == "0":
        menu()
    else:
        configura_dispositivos()
        pause()
        

def pause():
    print()
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
        conn = None
        try:
            print(LINE)
            rprint(f"[green]DEVICE: {device['host']} | Versao OS: {device['device_type']} | NAME: {device['device_name']} | FABRICANTE: {device['vendor']}[/green]")
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
            
        except Exception as e:
            rprint(f"[red]Não foi possivel conectar ao dispositivo ❌ ({type(e).__name__})[/red]")
        finally:
            if conn:
                try:
                    conn.disconnect()
                except Exception as e:
                    rprint(f"[red]Erro ao desconectar do dispositivo: {type(e).__name__}[/red]")    


def renderiza_template(caminho_template, info_configs):
    with open(CAMINHO_TEMPLATE, 'r') as arquivo:
        config = arquivo.read()
        config_renderizada = Template(config).render(**info_configs)
        rprint("Renderizando...")
        comandos = []
        for linha in config_renderizada.splitlines():
            if linha:
                comandos.append(linha)
        rprint("Configs renderizada")
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
        interface = input('Entre com o nome da interface (Ex: eth0/2, ...) ')
        info_configs = {'vlan_id': vlan_id, 'vlan_nome' : vlan_nome ,'interface': interface}

        comandos = renderiza_template(CAMINHO_TEMPLATE,info_configs)
        

        for device in DEVICES:
            if ip == device['host']:
                conn = None
                try:
                    print(LINE)
                    rprint(f"[green]DEVICE: {device['host']} | Versao OS: {device['device_type']} | NAME: {device['device_name']} | FABRICANTE: {device['vendor']}[/green]")
                    print(LINE)
                    conn = conecta_dispositivos(device)
                    if device['device_type'] == "cisco_ios":
                        resultado_cmds = conn.send_config_set(comandos)
                        print(resultado_cmds)
                    elif device['device_type'] == "arista_eos":
                        resultado_cmds = conn.send_config_set(comandos)
                        print(resultado_cmds)
                    rprint(f"[bold green]Configuração aplicada [/bold green]")

                except Exception as e:
                    rprint(f"[red]Não foi possivel conectar ao dispositivo ❌[/red]\n {e}")
                
                finally:
                    if conn:
                        conn.disconnect()
    else:                    
        rprint(f"[red]IP digitado não existe no inventário![/red]!!")


def normaliza_mac(mac):
    mac = mac.replace(".", "").replace(":", "").replace("-", "").lower()
    if len(mac) != 12:
        rprint(f"[red]Formato de MAC inválido![/red]")
        return None
    return f"{mac[0:4]}.{mac[4:8]}.{mac[8:12]}"



def localiza_mac(): 
    cmd_mac_cisco = "show mac address-table"
    cmd_mac_arista = "show mac address-table"
       
    mac_usuario = input("\nEntre com o MAC (ex: aaaa.bbbb.cccc): ").strip()
    mac_normalizado = normaliza_mac(mac_usuario)
    if not mac_normalizado:
        return 
    
    mac_usuario = mac_normalizado
    mac_encontrado_em_algum_device = False

    for device in DEVICES:
        conn = None
        try: 
            conn = conecta_dispositivos(device)

            if device['device_type'] == "cisco_ios":
                resultado_cmd = conn.send_command(cmd_mac_cisco, use_textfsm=True)
                #print("Cisco:", resultado_cmd)
            elif device['device_type'] == "arista_eos":
                resultado_cmd = conn.send_command(cmd_mac_arista, use_textfsm=True)
                #print("Arista:", resultado_cmd)
            
            print("-" * 80)
            rprint(f"Checando MAC em {device['device_name']}")        
            print("-" * 80)
            for mac in resultado_cmd:
                mac_encontrado = mac.get('destination_address') or mac.get('mac_address')
                vlan_id = mac.get('vlan_id') 
                dst_port = mac.get('destination_port') or mac.get('port')

                if mac_usuario == mac_encontrado:
                    mac_encontrado_em_algum_device = True
                    rprint(f"[bold green]MAC ADDRESS : {mac_usuario} encontrado no dispositivo:\n{device['device_name']}({device['host']}[/bold green])")
                    rprint(f"[bold green ]VLAN_ID: {vlan_id}[/bold green]")
                    rprint(f"[bold green]DESTINATION PORT: {dst_port}[/bold green]")
                    print()
                    

        except Exception as e:
            print("-" * 80)
            rprint(f"[red]Falha ao conectar em {device['device_name']} ({type(e).__name__})\n{e}[/red]")
        
        finally:
            if conn:
                conn.disconnect()

    if not mac_encontrado_em_algum_device:
        rprint(f"\n❌MAC ADDRESS : {mac_usuario} não encontrado na rede!")
        

def bkp_configs():
    os.system('clear')
    DIR_BKP = "./Trilha Python/backups"
    c_sucesso = 0
    c_falha = 0
    
    if not os.path.exists(DIR_BKP):
        os.makedirs(DIR_BKP)
    total_devices = len(DEVICES)

    with Progress(
        SpinnerColumn(style="white"),
        TextColumn("[bold white]Backing up configs[/bold white]"),
        BarColumn(bar_width=40),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("•"),
        TextColumn("{task.completed}/{task.total}"),
        TextColumn("•"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:

        task = progress.add_task(
            "[green]Iniciando backup das configurações[/green]",
            total=total_devices,
        )    
        for device in DEVICES:
            CAMINHO_BKP = os.path.join(DIR_BKP, f"bkp_{device['device_name']}.cfg") 
            conn = None
            try:
                conn = conecta_dispositivos(device)
                if device['device_type'] == "cisco_ios":
                    config = conn.send_command("show running-config")
                    with open(CAMINHO_BKP, "w") as arquivo:
                        arquivo.write(config)
                    rprint(f"[green] ->Backup realizado com sucesso para {device['device_name']}[/green]")
                    c_sucesso += 1
                elif device['device_type'] == "arista_eos":
                    config = conn.send_command("show running-config")
                    with open(CAMINHO_BKP, "w") as arquivo:
                        arquivo.write(config)
                    rprint(f"[green] ->Backup realizado com sucesso para {device['device_name']}[/green]")
                    c_sucesso += 1
                
            except Exception as e:
                rprint(f"[red] ->Falha ao realizar backup em {device['device_name']} ({type(e).__name__}).[/red]")
                c_falha += 1
            finally:
                progress.advance(task , 1)
                if conn:
                    conn.disconnect()
                
                
    rprint(
        f"\n[bold green]✔ Backup finalizado![/bold green]"
        f"\n✅ {c_sucesso} dispositivos processados com sucesso\n"
        f"\n❌ {c_falha} dispositivos processados com falha\n"
    )
    print()
    pause()


def main():
    os.system('clear')
    while True:
        app_info()
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            coleta_informacoes()
            pause()
        elif opcao == "2":
            app_info()
            localiza_mac()
            pause()
        elif opcao == "3":
            app_info()
            menu_config()
        elif opcao == "4":
            bkp_configs()
        elif opcao == "0":
            break
        else:
            print()
            rprint(f"[red]Opção não valida no menu!!![/red]")
            print()
            pause()


if __name__ == "__main__":
    main()

