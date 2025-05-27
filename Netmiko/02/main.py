from netmiko import ConnectHandler
from rich import print as rprint
from inventario import DEVICES

for device in DEVICES:
    print(f"\nConectando ao dispositivo: {device['host']}...")
    with ConnectHandler(**device) as conn:
        # Coleta do show version
        cmd_output = conn.send_command("show version")
        lines = cmd_output.splitlines()
        #Encontrar linha com versão
        for line in lines:
            if "Cisco IOS Software" in line:
                version_line = line.strip().split()[7].split(",")[0]
                rprint(f"Cisco IOS Version: {version_line}")
                break
            if "Software image version" in line:
                version_line = line.strip().split(":")[1].strip()
                rprint(f"Arista EOS Version: {version_line}")
                break  
        
