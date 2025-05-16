# Automatize Switches Cisco com Python + Nornir + Netmiko + Jinja2

Este projeto demonstra como automatizar a configuração de múltiplos switches Cisco usando Python, Nornir, Netmiko e Jinja2.

## Funcionalidades

- Carrega dados por host a partir de arquivos YAML
- Renderiza templates CLI com Jinja2
- Envia comandos via SSH com Netmiko
- Coleta comandos de validação
- Gera logs individuais por dispositivo

## Estrutura

```
.
├── switch_automation.py
├── templates/
│   ├── access_switch.j2
│   └── core_switch.j2
├── host_vars/
│   ├── core_switch.yaml
│   └── sw1.yaml
│   └── sw2.yaml
│   └── sw3.yaml
│   └── sw4.yaml
│   └── sw5.yaml
│   └── sw6.yaml
│   └── sw7.yaml
│   └── sw8.yaml
│   └── sw9.yaml
│   └── sw10.yaml
├── inventories/
│   ├── defaults.yaml
│   └── groups.yaml
│   └── hosts.yaml
├── logs/
└── requirements.txt
└── config.yaml
```

## Execução

```bash
pip install -r requirements.txt
python main.py
```

