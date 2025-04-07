# Arquivos e Scripts de videos do CanalYoutube

Este diretório contém os arquivos usados no vídeo [Automação de Redes com Python na prática: Colete dados em Minutos](https://www.youtube.com/watch?v=VAx9g35QQbQ).

---

## 📋 O que você vai aprender

- Como usar o **Netmiko** para se conectar a dispositivos Cisco e Arista.
- Como enviar comandos remotamente via SSH.
- Como coletar informações como **hostname, versão do sistema e número de série**.
- Como salvar os dados em um **arquivo CSV** automaticamente.

---

## 📂 Arquivos incluídos

| Arquivo               | Descrição                                      |
|-----------------------|-----------------------------------------------|
| `script_netmiko_01.py`| Script principal que conecta aos dispositivos |

---

## ▶️ Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   python3 script_netmiko_01.py 