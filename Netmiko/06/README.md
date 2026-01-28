# NetAutomation CLI Toolkit 🚀

Ferramenta em Python desenvolvida na série **Trilha Python para Profissionais de Rede**.

## 📌 Funcionalidades
- Coleta de informações de dispositivos Cisco e Arista
- Localização de MAC Address em múltiplos switches
- Backup automático de configurações
- Configuração de VLAN via template Jinja2
- Barra de progresso profissional com Rich

## 🛠 Tecnologias
- Python 3.10+
- Netmiko
- Rich
- Jinja2
- dotenv

## 📂 Estrutura
- `devices_inventory.py` → Inventário de dispositivos
- `templates/` → Templates Jinja2
- `backups/` → Backups gerados automaticamente
- `python_ep6.py` → Aplicação principal (CLI)

## ▶️ Como executar
```bash
pip install -r requirements.txt
python main.py