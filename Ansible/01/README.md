# Arquivos e Scripts de videos do CanalYoutube

Este diretório contém os arquivos usados no vídeo ["Ansible? O que todo o Profissional de Redes deveria saber em menos de 20 minutos!"](https://youtu.be/ayWVJpfS9hI?si=lTEl4XhvHGSOj8Pp).

---

## 📋 O que você vai aprender
✅ O que é Ansible e como ele funciona nos bastidores

✅ A diferença entre linguagem declarativa e imperativa

✅ Como criar um playbook simples, reutilizável e escalável

✅ Como automatizar o backup de  configuração dos equipamentos Cisco e Arista com Ansible

---

## 📂 Arquivos incluídos

| Arquivo              | Descrição                                              |
|----------------------|--------------------------------------------------------|
| `ansible.cfg`      | Arquivo de configuração de parametros globais do Ansible |
| `inventory.ini`    | Inventário dos dispositivos de rede do Ansible           |
| `playbook_bkp.yaml`| Playbook para execução de tarefas para o Ansible         |

---

## ▶️ Como executar

1. cd Diretorio (arquivos Ansible)
   ansible-playbook playbook_bkp.yaml
