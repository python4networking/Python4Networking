# Automação Completa de Rede com Ansible – Episódio 3 

Este repositório contém o playbook completo desenvolvido nos episódio 3 da série **Ansible para Profissionais de Rede**, do canal [Python4Networking](https://www.youtube.com/@Python4Networking).

---
### 📍 Episódios 1,2 e 3

- Coleta dos comandos:
  - `show version`
  - `show ip interface brief`
- Uso do módulo `ansible.netcommon.cli_command`
- Exibição das saídas usando `debug`
- Aplicação automática de VLANs em Switches de Acesso
- Uso de template Jinja2: `config_vlans_acesso.j2` e `config_vlans_core.j2` 
- Criação de VLANs e SVIs (Interface VLAN) no Switch Core
- Configuração de trunk links para os Switches de Acesso no Switch Core
- Aplicação com `cisco.ios.ios_config` com backup

---
## 📂 Estrutura do Projeto

```
ansible-core/
├── inventory/
│   └── hosts.yml               # Inventário de hosts
├── group_vars/
│   ├── all.yml                 # Variáveis para todos os switchesswitches de acesso
├── templates/
│   ├── config_vlans_acesso.j2  # Template switches de acesso
│   └── config_vlans_core.j2    # Template switch core
├── playbooks/
│   └── playbook_ep3_all.yml    # Playbook completo (episódios 1-2-3)
└── README.md
```

---

## ▶️ Como Executar

```bash
ansible-playbook playbooks/playbook_ep3_all.yml
```

---

## 📺 Canal no YouTube

Assista ao passo a passo completo no canal [Python4Networking](https://www.youtube.com/@Python4Networking).

---

## 💬 Contribuições

Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorias!


