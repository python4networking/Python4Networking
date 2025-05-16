# Automatize Switches Cisco com Python + Netmiko + Jinja2

Este projeto demonstra como automatizar a configuração de múltiplos switches Cisco usando Python, Netmiko e Jinja2, sem frameworks adicionais como o Nornir.

## Funcionalidades

- Carrega dados por host a partir de arquivos YAML
- Renderiza templates CLI com Jinja2
- Envia comandos via SSH com Netmiko
- Coleta comandos de validação
- Gera logs individuais por dispositivo

## Estrutura

```
.
├── main.py
├── templates/
│   ├── access_switch.j2
│   └── core_switch.j2
├── host_vars/
│   ├── sw1.yaml
│   └── core.yaml
├── logs/
└── requirements.txt
```

## Execução

```bash
pip install -r requirements.txt
python main.py
```

