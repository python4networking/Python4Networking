# Episódio 3 – Enviando Configurações com Netmiko 

Este episódio faz parte da trilha **Python Básico para Profissionais de Redes** do canal [Python4Networking](https://www.youtube.com/@Python4Networking).

## 🎯 Objetivo
Demonstrar como **enviar configurações para dispositivos de rede Cisco** usando **Python + Netmiko 4.x**, aplicando boas práticas com o **Context Manager (`with`)**.

## 🧩 O que você aprenderá
- Conexão SSH com `ConnectHandler`
- Envio de comandos de configuração (`send_config_set`)
- Envio de blocos via arquivo (`send_config_from_file`)
- Salvamento da configuração (`save_config`)
- Encerramento automático da sessão (Context Manager)

## 📂 Estrutura dos arquivos
```
episodio3_netmiko_context_manager/
├── python_ep3.py
├── configs_r1.txt
└── README.md
```

## ▶️ Execução
```bash
pip install netmiko rich
python python_ep3.py
```

## 💡 Dicas
- Use o `with ConnectHandler` sempre que possível — é a forma **mais limpa e segura** de lidar com conexões SSH.
- Evite deixar credenciais no código; use variáveis de ambiente em produção.
- Esse mesmo padrão pode ser expandido para **vários dispositivos** em um loop.

---

🧑‍💻 **Canal:** [Python4Networking](https://www.youtube.com/@Python4Networking)  
📺 **Episódio 3 – Enviando Configurações com Netmiko**
