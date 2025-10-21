#!/usr/bin/env python3
"""
Script de configuração inicial do bot de despesas
"""

import os
import sys

def create_env_file():
    """Cria o arquivo .env se não existir"""
    env_file = '.env'
    
    if os.path.exists(env_file):
        print("✅ Arquivo .env já existe")
        return
    
    print("📝 Criando arquivo .env...")
    
    env_content = """# Token do seu bot do Telegram
# Obtenha este token criando um bot com @BotFather no Telegram
BOT_TOKEN=seu_token_aqui
"""
    
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Arquivo .env criado com sucesso!")
        print("⚠️  Lembre-se de substituir 'seu_token_aqui' pelo token real do seu bot")
    except Exception as e:
        print(f"❌ Erro ao criar arquivo .env: {e}")

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print("🔍 Verificando dependências...")
    
    try:
        import telebot
        import dotenv
        print("✅ Todas as dependências estão instaladas")
        return True
    except ImportError as e:
        print(f"❌ Dependência não encontrada: {e}")
        print("💡 Execute: pip install -r requirements.txt")
        return False

def main():
    """Função principal"""
    print("🚀 Configuração do Bot de Despesas")
    print("=" * 40)
    
    # Criar arquivo .env
    create_env_file()
    
    # Verificar dependências
    if not check_dependencies():
        print("\n❌ Instale as dependências antes de continuar:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    print("\n✅ Configuração concluída!")
    print("\n📋 Próximos passos:")
    print("1. Edite o arquivo .env e adicione seu token do bot")
    print("2. Execute: python bot.py")
    print("3. Teste o bot no Telegram com /start")

if __name__ == '__main__':
    main()
