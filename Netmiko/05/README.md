# Python4Networking – Trilha Python para Profissionais de Redes do Zero  

Este repositório faz parte da série **Trilha Python para Profissionais de Redes do Zero**, publicada no canal **Python4Networking**.

No **Episódio 5**, evoluímos o CLI Toolkit criado nos episódios anteriores e implementamos **configuração de dispositivos de rede utilizando templates Jinja2**, aplicados via **Netmiko** em switches **Cisco** e **Arista**.

---

## 🎯 Objetivo do Episódio 5

Demonstrar, de forma **didática e prática**, como:
- organizar um script Python para automação de redes
- separar lógica de automação e configuração
- gerar configurações dinamicamente usando **Jinja2**
- aplicar configurações reais em dispositivos de rede

Este episódio marca a transição de **scripts básicos** para uma **automação mais profissional e reutilizável**.

---

## 🧠 O que você aprende neste repositório

✔ Criação da função `configura_dispositivos()`  
✔ Criação da função `renderiza_template()`  
✔ Uso de templates Jinja2 em arquivos `.j2`  
✔ Renderização dinâmica de configuraações de rede  
✔ Conversão de template em lista de comandos  
✔ Aplicação de configurações com `send_config_set()`  
✔ Validação de dispositivos a partir do inventário  

---

## 🗂 Estrutura do Projeto

```
.
├── main.py                     # Script principal (CLI Toolkit)
├── devices_inventory.py        # Inventário de dispositivos (exemplo)
├── Trilha Python/
│   └── templates/
│       └── vlan.j2             # Template Jinja2 para configuração de VLAN
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Requisitos

- Python **3.9+**
- Acesso SSH aos dispositivos de rede

### 📦 Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## 📋 Inventário de Dispositivos

O arquivo `devices_inventory.py` contém uma exemplo da lista de dispositivos no formato:

```python
DEVICES = [
    {
        "device_type": "cisco_ios",
        "host": "IP_DISPOSITIVO",
        "username": "cisco",
        "password": "cisco",
        "device_name" : "Multilayer_Switch",
        "vendor": "Cisco"
    },
    {
        "device_type": "arista_eos",
        "host": "IP_DISPOSITIVO",
        "username": "admin",
        "password": "arista",
        "device_name" : "SW6",
        "vendor": "Arista"
    },
]
```
Ajustes os valores das chaves do `devices_inventory.py` de acordo com o seu ambiente.

> Dica: para laboratório, use **Containerlab / EVE-NG / GNS3** ou seu ambiente com switches reais.

---

## 🧩 Template Jinja2

### 📄 `Trilha Python/templates/vlan.j2`

```jinja2
vlan {{ vlan_id }}
name {{ vlan_nome }}
exit
interface {{ interface}}
switchport mode access
switchport access vlan {{ vlan_id }}

```

Este template permite (de forma didática):
- criar VLAN
- nomear a VLAN
- associar VLAN a interface

---

## ▶️ Como Executar

```bash
python3 python_ep5.py
```

### Menu principal:

```
1) Coleta de informações (Cisco/Arista)
2) Localizar MAC address na rede
3) Configuração de dispositivos
4) Backup de configurações
0) Sair
```

---

## 🔧 Fluxo da Configuração de Dispositivos (Ep.5)

1. Selecionar a opção **Configuração de dispositivos**
2. Informar o **IP do switch** (validado no inventário)
3. Informar:
   - VLAN ID
   - Nome da VLAN
   - Interface
4. O script:
   - renderiza o template Jinja2
   - transforma o resultado em lista de comandos
   - aplica a configuração via Netmiko

---

## 🚀 Tecnologias Utilizadas

- **Python**
- **Netmiko**
- **Jinja2**
- **Rich**
- **Cisco IOS**
- **Arista EOS**

---

## 📚 Trilha Python para Profissionais de Redes

Este repositório faz parte de uma trilha progressiva:

- ✅ Ep.1-3 – Conceitos fundamentais
- ✅ Ep.4   – Funções e CLI Toolkit  
- ✅ Ep.5   – Configuração com Jinja2  
- ⏭️ Próximo: inserção das funções: Backup de configurações + Localização de mac

---

## 🛑 Aviso Importante

> ⚠️ Este código é **educacional**.  
> Em ambientes de produção, utilize: controle de mudanças, versionamento, logs e validações pré/pós-change.

---

## 📺 Canal no YouTube

📌 **Python4Networking**  
Conteúdo prático e direto para profissionais de redes que querem aprender automação **do zero até o nível profissional**.

Se este projeto te ajudou:
⭐ deixe uma estrela no repositório  
👍 curta o vídeo  
💬 deixe seu comentário no YouTube



