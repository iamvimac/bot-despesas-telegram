import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print("⚠️  ATENÇÃO: Token do bot não encontrado!")
    print("Crie um arquivo .env na raiz do projeto com:")
    print("BOT_TOKEN=seu_token_aqui")
    print("Obtenha o token criando um bot com @BotFather no Telegram")
