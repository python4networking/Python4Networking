
# ==========================================================
# Trilha - Python Básico para Profissionais de Redes
# EPISÓDIO 3: Enviando Configurações com Netmiko
# Automação de Redes com Python
# ==========================================================

from netmiko import ConnectHandler
from rich import print as rprint

# ----------------------------------------------------------
# Dicionário do dispositivo
# ----------------------------------------------------------
cisco_r1 = {
    "device_type": "cisco_ios",
    "ip": "ENDEREÇO_IP",
    "username": "USERNAME",
    "password": "PASSWORD",
}

# ----------------------------------------------------------
# Context Manager (forma mais limpa e segura)
# ----------------------------------------------------------
rprint("[bold cyan]Conectando ao dispositivo...[/bold cyan]")

with ConnectHandler(**cisco_r1) as connect:
    rprint("[green]Conexão estabelecida com sucesso![/green]\n")

    # ------------------------------------------------------
    # Enviando comandos de configuração em lista
    # ------------------------------------------------------
    comandos_config = [
        "interface loopback10",
        "ip address 10.10.10.10 255.255.255.255",
        "description Loopback criada via Python",
    ]
    rprint("[yellow]Enviando configuração de interface...[/yellow]")
    output = connect.send_config_set(comandos_config)
    rprint(output)

    # ------------------------------------------------------
    # Enviando configurações a partir de um arquivo externo
    # ------------------------------------------------------
    rprint("\n[yellow]Enviando configurações a partir de arquivo...[/yellow]")
    output = connect.send_config_from_file("configs_r1.txt")
    rprint(output)

    # ------------------------------------------------------
    # Salvando configuração
    # ------------------------------------------------------
    rprint("[yellow]Salvando configuração...[/yellow]")
    save_output = connect.save_config()
    rprint(save_output)

rprint("\n[bold green]Configuração concluída e conexão encerrada![/bold green]")
