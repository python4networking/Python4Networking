# ==========================================================
# Trilha - Python Básico para Profissionais de Redes
# EPISÓDIO 2: Loops, Condicionais, Netmiko
# Automação de Redes com Python - Episódio 2
# Objetivo: Conectar em múltiplos dispositivos, coletar comandos
#           e extrair a versão do sistema operacional
# ==========================================================

#------------------------------------------------------------------------------------------
## Código Final 
#------------------------------------------------------------------------------------------
from netmiko import ConnectHandler
from rich import print as rprint

# Inventário de dispositivos (lista de dicionários)
DISPOSITIVOS = [
    {
        "device_type": "cisco_ios",
        "host": "ENDEREÇO_IP_DISPOSITIVO_DE_REDE",
        "username": "USERNAME",
        "password": "SENHA",
    },
        {
        "device_type": "cisco_ios",
        "host": "ENDEREÇO_IP_DISPOSITIVO_DE_REDE",
        "username": "USERNAME",
        "password": "PASSWORD",
    },
        {
        "device_type": "cisco_ios",
        "host": "ENDEREÇO_IP_DISPOSITIVO_DE_REDE",
        "username": "USERNAME",
        "password": "PASSWORD",
    },
    {
        "device_type": "cisco_ios",
        "host": "ENDEREÇO_IP_DISPOSITIVO_DE_REDE",
        "username": "USERNAME",
        "password": "PASSWORD",
    },
{
        "device_type": "arista_eos",
        "host": "ENDEREÇO_IP_DISPOSITIVO_DE_REDE",
        "username": "USERNAME",
        "password": "PASSWORD",
    },
{
        "device_type": "arista_eos",
        "host": "ENDEREÇO_IP_DISPOSITIVO_DE_REDE",
        "username": "USERNAME",
        "password": "PASSWORD",
    }
]

# Lista de comandos genéricos a serem executados
COMANDOS = ["show ip interface brief"]

# Loop nos dispositivos
for dispositivo in DISPOSITIVOS:
    rprint(f"\n[bold green]Conectando ao dispositivo: {dispositivo['host']}[/bold green]...")
    
    # Conexão SSH
    with ConnectHandler(**dispositivo) as conn:
        
        # Executa comandos da lista
        for cmd in COMANDOS:
            output = conn.send_command(cmd)

            # Condição: alerta se houver interfaces down
            if "down" in output:
                rprint(f"[red]{cmd} Detectou interfaces down[/red]")
            else:
                rprint(f"[cyan]{cmd} Executado com sucesso[/cyan]")

            rprint(output, "\n")

        # Extraindo versão do sistema operacional
        cmd_output = conn.send_command("show version")
        linhas = cmd_output.splitlines()
        for linha in linhas:
            if "Cisco IOS Software" in linha:  # Para Cisco
                versao_cisco = linha.strip().split()[7].split(",")[0]
                rprint(f"[bold yellow]Versão do Cisco IOS: [/bold yellow] {versao_cisco}")
                break

            if "Software image version" in linha:  # Para Arista
                versao_arista = linha.strip().split(":")[1].strip()
                rprint(f"[bold yellow]Versão do Arista EOS:[/bold yellow] {versao_arista}")
                break











