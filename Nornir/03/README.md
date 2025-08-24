# 🚀 NetBox + Python (Nornir + Napalm) na Prática: Backup Automático com Inventário Dinâmico!

[![YouTube Video](https://img.shields.io/badge/🎥%20Assistir%20no%20YouTube-Python4Networking-red?style=for-the-badge&logo=youtube)](https://youtube.com/watch?v=OjtyooYy2TU)

Este repositório contém um exemplo prático de como utilizar o **NetBox como inventário dinâmico** com **Python**, usando os frameworks **Nornir** e **Napalm**, para realizar **backup automatizado de configurações de dispositivos Cisco e Arista**.

---

## 📦 Estrutura do Projeto

```
.
├── main.py                  # Script principal (execução do backup)
├── .env.example            # Arquivo de exemplo com credenciais por fabricante
├── Nornir_Netbox/
│   └── config.yaml         # Configuração do Nornir com inventário via NetBox
├── Backups/                # Pasta onde serão salvos os arquivos de configuração
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Acesso a um NetBox ativo e populado com dispositivos
- Token de autenticação no NetBox
- Instalar as dependências com:

```bash
pip install nornir nornir-napalm nornir-netbox rich python-dotenv
```

---

## 🚀 Como Usar

1. Copie o arquivo `.env.example` para `.env` e configure suas credenciais:
```ini
CISCO_USERNAME=seu_usuario
CISCO_PASSWORD=sua_senha

ARISTA_USERNAME=admin
ARISTA_PASSWORD=arista
```

2. Edite o arquivo `Nornir_Netbox/config.yaml` com a URL e token do seu NetBox

3. Execute o script:
```bash
python main.py
```

---

## ✅ O que acontece

- O script identifica automaticamente se o dispositivo é Cisco (`ios`) ou Arista (`eos`)
- Aplica as credenciais corretas via `.env`
- Coleta o `running-config` usando Napalm
- Salva o resultado em um arquivo `.txt` com timestamp

---

## 🎯 Resultado Esperado

- Backups salvos em:
  ```
  ./Backups/Bkp_R1_2025-08-22_15-30-00.txt
  ```

---

## 📺 Assista vídeo desse conteúdo e outros completo no canal

> Neste vídeo eu explico **o que é o NetBox**, por que ele é tão importante na automação de redes, e como ele se conecta com **Nornir, Napalm e Python** para entregar um fluxo real de automação profissional.

🎬 **Link:** [YouTube - Python4Networking](https://youtube.com/@python4networking)

---

## 👨‍💻 Desenvolvido por:
**Glaucio Giesen**  
Canal: [Python4Networking](https://youtube.com/@python4networking)

