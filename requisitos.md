Chatbot de Controle de Despesas
📋 Sobre o Projeto
Bot do Telegram para controle de despesas em Python usando pyTelegramBotAPI.

🎯 Objetivo
Versão inicial simples - o bot deve responder comandos básicos e repetir o texto do comando /despesa.

🛠 Tecnologias
Python

pyTelegramBotAPI

Variáveis de ambiente

📝 Funcionalidades
Comandos Implementados
/start - Mensagem de boas-vindas

/hello - Saudação

/despesa [texto] - Repete o texto enviado pelo usuário

🗂 Estrutura de Arquivos
text
meu-bot-despesas/
├── bot.py
├── .env
├── requirements.txt
└── README.md
🔧 Configuração Rápida
1. Criar Bot no Telegram
Buscar @BotFather no Telegram

Enviar /newbot

Seguir instruções e guardar o token

2. Preparar Ambiente
bash
# Criar e ativar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependências
pip install pyTelegramBotAPI python-dotenv
3. Arquivo .env
env
BOT_TOKEN=seu_token_aqui
4. Código do Bot (bot.py)
python
import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou seu bot de despesas. Use /despesa para registrar um gasto.")

@bot.message_handler(commands=['despesa'])
def handle_expense(message):
    # Remove o comando e pega o texto restante
    user_text = message.text.replace('/despesa', '').strip()
    if user_text:
        bot.reply_to(message, f"Você registrou: {user_text}")
    else:
        bot.reply_to(message, "Por favor, adicione informações após o comando /despesa")

if __name__ == '__main__':
    print("Bot está rodando...")
    bot.infinity_polling()
5. requirements.txt
text
pyTelegramBotAPI
python-dotenv
🚀 Como Usar
Execute o bot: python bot.py

No Telegram, envie:

/start - para iniciar

/despesa 25.50 Café Padaria - o bot repetirá "25.50 Café Padaria"

✅ Próximos Passos
Testar configuração básica

Verificar resposta dos comandos

Validar segurança do token