# Episódio 02 – Ansible para Profissionais de Rede

## 🎯 Tema: Configuração de VLANs nas Interfaces dos Switches de Acesso

Este repositório contém os arquivos demonstrados no Episódio 02 da série **“Ansible para Profissionais de Rede – Primeiros Playbooks”**, publicada no canal [Python4Networking](https://www.youtube.com/@python4networking).

O foco deste episódio é mostrar como automatizar, de forma escalável, a **configuração de interfaces de switches com VLANs específicas usando Ansible e Jinja2**.

---

## 📁 Estrutura de Diretórios
```text
├── inventory.ini # Inventário Ansible com switches
├── host_vars/ # Variáveis por Switch
│ ├── sw01.yml
│ ├── sw02.yml
│ └── ... até sw10.yml
├── templates/
│ └── config_vlans.j2 # Template Jinja2 para as interfaces
├── playbook_ep2.yml # Playbook principal
└── README.md # Este arquivo
```

---

📘 Como Executar

Configure o inventário inventory.ini com IPs e credenciais dos switches.
Ajuste os arquivos host_vars/swXX.yml com a VLAN e interface correspondente.
Execute o playbook:
```bash
ansible-playbook playbook_ep2.yml
```

▶️ [Assista ao Episódio no YouTube](https://youtu.be/AGzdTNNq6tg)
🎥 *Seu Primeiro Playbook Ansible na Rede – Automatize VLANs em Switches com Ansible  (Episodio 2)

🧑‍💻 Canal Python4Networking
Se você é profissional de redes e quer aprender a automatizar sua infraestrutura com Python, Ansible e outras ferramentas modernas, inscreva-se no canal e acompanhe a série completa.

🛠️ Requisitos
Python 3.8+
Ansible 2.15+
Acesso SSH (CLI) aos switches Cisco



