# 📘 Variáveis e Strings em Python com Aplicação em Redes

Este repositório contém o código-fonte e materiais utilizados no vídeo **"Variáveis e Strings Python com Netmiko: Aprenda na Prática!"** do canal [Python4Networking](https://youtu.be/wGFoWdQY8ZA).

## 📌 Conteúdo do vídeo

Neste vídeo, você aprende:
- O que são variáveis e strings em Python
- Métodos úteis de strings: `.strip()`, `.splitlines()`, `.split()` etc.
- Como coletar a versão do IOS (Cisco) e EOS(Arista) usando Netmiko
- Aplicação prática com manipulação de strings reais

## 📁 Arquivos

- `main.py` – Script para coletar o output do `show version` e extrair a versão do IOS e EOS

## 🚀 Como rodar o script

1. Instale as dependências:
```bash
pip install netmiko
```

2. Execute o script:
```bash
python main.py
```

> ⚠️ Certifique-se de ajustar os IPs e credenciais no arquivo `inventario.py`.


