# Episódio 01 – Seu Primeiro Playbook com Ansible

🎥 Série: **Ansible Profissionais de Rede **  
🔗 Playlist: [(https://www.youtube.com/playlist?list=PLYyNXSDvdcqxlgryctRUwTcJ2A3s3Ta22)]

---

## 🎯 Objetivo do Episódio
Neste episódio, você aprenderá a criar seu **primeiro playbook com Ansible** voltado para automação de redes, com foco em **coleta de informações básicas de dispositivos Cisco**, como:

- `show version`
- `show ip interface brief`

Tudo de forma simples e didática, ideal para quem está **começando com Ansible em ambientes de rede.**

---

## 📂 Estrutura do Projeto

```
02/
├── README.md
├── inventory.ini
├── playbook_ep1.yml

```

---

## ⚙️ Requisitos

- Python 3.8+
- Ansible instalado (`pip install ansible`)

---

## 🚀 Como executar

```bash
ansible-playbook playbook_ep1.yml
```

---

## 📘 Inventário de exemplo (`inventory.ini`)
```ini
[cisco]
SW1 ansible_host=ENDEREÇO_IP
SW2 ansible_host=ENDEREÇO_IP

[cisco:vars]
ansible_user=USERNAME
ansible_password=PASSWORD
ansible_network_os=cisco.ios.ios
ansible_connection=network_cli
```

---

## 🙋‍♂️ Sobre a Série

Essa série foi criada especialmente para profissionais de redes que desejam aprender automação de forma prática, mesmo sem experiência prévia com Ansible ou programação.

📡 Do zero à automação real em poucos episódios.

---

👨‍🏫 Canal: [Python4Networking](https://www.youtube.com/@python4networking)