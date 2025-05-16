# Arquivos e Scripts de videos do CanalYoutube

Este diretório contém os arquivos usados no vídeo ["Configure +10 SWITCHES em Segundos com Python!!!"](https://youtu.be/Kbd_7KYEPYw).

---

## O que você vai aprender:

- Como usar YAML para dados de switches
- Gerar comandos (templates) automaticamente com Jinja2
- Enviar configs via Netmiko (SSH)
- Coletar show commands automaticamente
- Gerar logs completos por equipamento

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

