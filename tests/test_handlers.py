from types import SimpleNamespace
import importlib


def make_message(text: str, first_name: str = "Tester"):
    # Estrutura mínima para simular message do TeleBot
    return SimpleNamespace(
        text=text,
        from_user=SimpleNamespace(first_name=first_name),
    )


def test_send_welcome(monkeypatch):
    bot = importlib.import_module("bot")

    sent = {}

    def fake_reply(message, text):
        sent["text"] = text

    msg = make_message("/start")
    monkeypatch.setattr(bot, "bot", SimpleNamespace(reply_to=fake_reply))

    bot.send_welcome(msg)

    assert "Olá! Eu sou seu bot de controle de despesas" in sent["text"]
    assert "/despesa" in sent["text"]


def test_handle_expense_with_text(monkeypatch):
    bot = importlib.import_module("bot")

    sent = {}

    def fake_reply(message, text):
        sent["text"] = text

    msg = make_message("/despesa 25.50 Café Padaria Cartão")
    monkeypatch.setattr(bot, "bot", SimpleNamespace(reply_to=fake_reply))

    bot.handle_expense(msg)

    assert "💰 Despesa registrada: 25.50 Café Padaria Cartão" == sent["text"]


def test_handle_expense_without_text(monkeypatch):
    bot = importlib.import_module("bot")

    sent = {}

    def fake_reply(message, text):
        sent["text"] = text

    msg = make_message("/despesa")
    monkeypatch.setattr(bot, "bot", SimpleNamespace(reply_to=fake_reply))

    bot.handle_expense(msg)

    assert "Por favor, adicione informações" in sent["text"]
    assert "/despesa [valor]" in sent["text"]


def test_handle_other_messages(monkeypatch):
    bot = importlib.import_module("bot")

    sent = {}

    def fake_reply(message, text):
        sent["text"] = text

    msg = make_message("qualquer coisa")
    monkeypatch.setattr(bot, "bot", SimpleNamespace(reply_to=fake_reply))

    bot.handle_other_messages(msg)

    assert "Use os comandos disponíveis" in sent["text"]
    assert "/start" in sent["text"]
    assert "/despesa" in sent["text"]


