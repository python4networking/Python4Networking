🧰 Automação de Redes com Ansible + NetBox — Parte 2

Popular o NetBox automaticamente via API usando Ansible

Este repositório contém todos os arquivos utilizados no video "Automação de Redes com Ansible + NetBox — Parte 2", onde automatizamos completamente o cadastro de dispositivos dentro do NetBox utilizando Ansible.

O objetivo é mostrar como um engenheiro de redes pode deixar tarefas manuais para trás e começar a trabalhar com automação de forma profissional e escalável.

📌 📺 Conteúdo deste Vídeo

Nesta parte, você aprenderá a:

✔ Integrar o Ansible com o NetBox via API

✔ Criar sites, fabricantes, device types, plataformas, device roles

✔ Cadastrar dispositivos (Routers e Switches)

✔ Criar interfaces de rede automaticamente

✔ Criar endereços IP e associar a interfaces

✔ Definir o primary IP de cada device

✔ Transformar seu NetBox em um verdadeiro Source of Truth

Tudo isso via um único playbook — totalmente automatizado.

📁 Estrutura do Projeto

│── playbook1.yml                 # Playbook principal (PLAY1)
│── ansible.cfg                   # Configuração do Ansible
└── vars/
      └── play1_data.yml          # Dados usados para popular o NetBox automaticamente

🚀 Requisitos
📦 Instalação do Ambiente Python e Dependências
Para garantir que o Ansible e o inventário dinâmico do NetBox funcionem corretamente, é recomendado criar um ambiente virtual e instalar todas as bibliotecas necessárias via requirements.txt.

1. Crie o arquivo requirements.txt na raiz do projeto:
ansible-core
ansible-pylibssh
pytz

2. Crie o ambiente virtual (venv)
python3 -m venv .venv

3. Ative o ambiente virtual
Linux/macOS:
source .venv/bin/activate

Windows (PowerShell):
.\.venv\Scripts\activate

4. Instale as dependências
pip install -r requirements.txt

5. Instale a coleção necessária para integração com o NetBox
ansible-galaxy collection install netbox.netbox


Antes de executar, você precisa ter:

🔹 NetBox instalado

Pode ser bare-metal, VM, Docker(Demonstrado na Parte 1).

🔹 Token de API ativo

No NetBox:
Admin → Users → Tokens

🔹 Variáveis de ambiente configuradas
export NETBOX_URL="http://SEU_IP:8000"
export NETBOX_TOKEN="SEU_TOKEN"


▶️ Como Executar

1. Execute o playbook
ansible-playbook playbook1.yml

O Ansible irá:

Criar sites no NetBox

Criar fabricantes e device types

Cadastrar R1, R2, R3, R4, SW1, SW2

Criar interfaces automaticamente

Criar IPs e associar às interfaces

Definir o primary_ip4

Todo o NetBox é preenchido automaticamente.

🧠 Por que isso é importante?

No dia a dia, muitos profissionais ainda mantêm:

❌ Planilhas manuais
❌ Inventários incompletos
❌ Documentação que nunca acompanha a realidade
❌ Cadastro de dispositivos feito “na mão”

Isso é improdutivo, cansativo e te impede de crescer na carreira.

Ao dominar automação com:

Python

Ansible

NetBox

APIs REST

…você começa a operar em um nível mais alto, com mais tempo, mais eficiência e mais valor profissional.

É assim que você deixa o operacional pesado para trás e evolui para papéis mais estratégicos.

📘 Arquitetura Conceitual

 - Instalar Netbox com containers Docker Compose no Redhat 9 (Parte 1)

 - PLAY 1 (este vídeo):
   Popular o NetBox automaticamente via API.

 - PLAY 2 (próximo vídeo — Parte 3):
   Usar o inventário dinâmico do NetBox com Ansible para automatizar a rede real.


🔗 Canal Python4Networking

🎥 YouTube: https://www.youtube.com/@Python4Networking

📸 Instagram: https://instagram.com/python4networking


