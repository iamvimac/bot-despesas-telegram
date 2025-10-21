import telebot
from config import BOT_TOKEN

# Verifica se o token foi configurado
if not BOT_TOKEN or BOT_TOKEN == 'seu_token_aqui':
    print("❌ Erro: Token do bot não configurado!")
    print("Crie um arquivo .env na raiz do projeto com:")
    print("BOT_TOKEN=seu_token_aqui")
    print("Obtenha o token criando um bot com @BotFather no Telegram")
    # Evita sair durante testes automatizados
    import os as _os
    if not _os.getenv("PYTEST_CURRENT_TEST"):
        exit(1)

# Inicializa o bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    Comando de boas-vindas
    """
    welcome_text = """
👋 Olá! Eu sou seu bot de controle de despesas!

📋 Comandos disponíveis:
• /start - Mostra esta mensagem de boas-vindas
• /hello - Saudação
• /despesa [texto] - Registra uma despesa

💡 Exemplo de uso:
/despesa 25.50 Café Padaria do João Cartão

Estou pronto para ajudar vocês a controlar os gastos! 💰
    """
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['despesa'])
def handle_expense(message):
    """
    Comando para registrar despesas
    """
    # Remove o comando e pega o texto restante
    user_text = message.text.replace('/despesa', '').strip()
    
    if user_text:
        # Repete o texto enviado pelo usuário
        response = f"💰 Despesa registrada: {user_text}"
        bot.reply_to(message, response)
        
        # Log para debug (opcional)
        print(f"Despesa registrada por {message.from_user.first_name}: {user_text}")
    else:
        # Se não há texto após o comando
        help_text = """
❌ Por favor, adicione informações após o comando /despesa

💡 Exemplo:
/despesa 25.50 Café Padaria do João Cartão

📝 Formato sugerido:
/despesa [valor] [descrição] [local] [forma de pagamento]
        """
        bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    """
    Responde a mensagens que não são comandos
    """
    response = """
🤖 Olá! Use os comandos disponíveis:

• /start - Para ver os comandos
• /despesa [texto] - Para registrar uma despesa

💡 Exemplo: /despesa 15.00 Almoço Restaurante Dinheiro
    """
    bot.reply_to(message, response)

if __name__ == '__main__':
    print("🚀 Bot de despesas iniciando...")
    print("📱 Conectando ao Telegram...")
    
    try:
        # Inicia o bot
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f"❌ Erro ao iniciar o bot: {e}")
        print("Verifique se o token está correto e se há conexão com a internet.")
