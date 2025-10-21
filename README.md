# 🤖 Bot de Controle de Despesas - Telegram

Um bot simples para o Telegram para controlar despesas domésticas.

## 📋 Sobre o Projeto

Bot do Telegram para controle de despesas em Python usando pyTelegramBotAPI. Versão inicial simples que responde comandos básicos e repete o texto do comando `/despesa`.

## 🎯 Objetivo

Criar um bot que receba informações de despesas e as repita de volta, preparando a base para futuras integrações com APIs de controle financeiro.

## 🛠 Tecnologias

- **Python 3.7+**
- **pyTelegramBotAPI** - Biblioteca para interação com a API do Telegram
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📝 Funcionalidades

### Comandos Implementados

- `/start` - Mensagem de boas-vindas com instruções
- `/hello` - Saudação
- `/despesa [texto]` - Registra uma despesa (repete o texto enviado)

## 🗂 Estrutura de Arquivos

```
telegram-bot/
├── bot.py              # Código principal do bot
├── config.py           # Configurações e carregamento de variáveis
├── requirements.txt    # Dependências do projeto
├── README.md          # Este arquivo
└── .env               # Variáveis de ambiente (criar manualmente)
```

## 🔧 Configuração Rápida

### 1. Criar Bot no Telegram

1. Busque `@BotFather` no Telegram
2. Envie `/newbot`
3. Siga as instruções e guarde o token fornecido

### 2. Preparar Ambiente

```bash
# Criar e ativar ambiente virtual (recomendado)
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configurar Token

Crie um arquivo `.env` na raiz do projeto:

```env
BOT_TOKEN=seu_token_aqui
```

**⚠️ IMPORTANTE:** Substitua `seu_token_aqui` pelo token real obtido do @BotFather.

## 🚀 Como Usar

### Executar o Bot

```bash
python bot.py
```

Você deve ver a mensagem:
```
🚀 Bot de despesas iniciando...
📱 Conectando ao Telegram...
```

### Comandos no Telegram

1. **Iniciar o bot:**
   ```
   /start
   ```

2. **Registrar uma despesa:**
   ```
   /despesa 25.50 Café Padaria do João Cartão
   ```

3. **Saudação:**
   ```
   /hello
   ```

## 💡 Exemplos de Uso

### Registro de Despesas

```
/despesa 15.00 Almoço Restaurante do Centro Dinheiro
/despesa 89.90 Supermercado Extra Cartão de Crédito
/despesa 12.50 Uber Casa-Trabalho PIX
/despesa 45.00 Farmácia Droga Raia Cartão de Débito
```

### Formato Sugerido

```
/despesa [valor] [descrição] [local] [forma de pagamento]
```

## 🔍 Funcionalidades Atuais

- ✅ Comandos básicos (`/start`, `/hello`, `/despesa`)
- ✅ Validação de entrada
- ✅ Mensagens de ajuda
- ✅ Tratamento de erros
- ✅ Logs no console
- ✅ Testes unitários automatizados
- ✅ Cobertura de código

## 🧪 Testes

### Executar Testes

```bash
# Executar todos os testes
python -m pytest

# Executar com cobertura de código
python -m pytest --cov=bot --cov-report=html

# Executar testes em modo verbose
python -m pytest -v
```

### Estrutura de Testes

```
tests/
├── conftest.py          # Configurações e fixtures
└── test_handlers.py     # Testes dos handlers do bot
```

### Cobertura de Código

Os testes cobrem:
- ✅ Handler de boas-vindas (`/start`, `/hello`)
- ✅ Handler de despesas (`/despesa`)
- ✅ Handler de mensagens genéricas
- ✅ Validação de entrada vazia

## ✅ Próximos Passos

- [x] Testar configuração básica
- [x] Verificar resposta dos comandos
- [x] Validar segurança do token
- [ ] Implementar integração com API de despesas
- [ ] Adicionar validação de formato de dados
- [ ] Implementar relatórios de despesas

## 🛡️ Segurança

- **NUNCA** compartilhe seu token do bot
- Mantenha o arquivo `.env` fora do controle de versão
- Use ambientes virtuais para isolar dependências

## 🐛 Solução de Problemas

### Bot não inicia

1. Verifique se o token está correto no arquivo `.env`
2. Confirme se há conexão com a internet
3. Verifique se todas as dependências foram instaladas

### Comandos não funcionam

1. Certifique-se de que o bot está rodando
2. Verifique se está enviando os comandos corretos
3. Confirme se o bot foi adicionado ao grupo/conversa

## 📞 Suporte

Se encontrar problemas, verifique:
1. Se o token está correto
2. Se as dependências estão instaladas
3. Se há conexão com a internet
4. Se o bot está ativo no Telegram

---

**Desenvolvido com ❤️ para controle de despesas domésticas**
