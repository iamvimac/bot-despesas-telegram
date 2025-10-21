import os
import pytest


@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    # Garante que o BOT_TOKEN esteja definido durante os testes
    monkeypatch.setenv("BOT_TOKEN", "test-token")
    yield

