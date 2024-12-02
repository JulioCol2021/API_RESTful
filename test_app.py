
"""
test_app.py
============================
Descrição:
Este módulo implementa funcionalidades de API RESTful para gerenciar uma lista de filmes.

Autores:
Desenvolvido por Julio Cesar da Silva Santos.

Modificações:
Atualizado com padrões Javadoc, princípios SOLID e Clean Code.
"""

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_intervals_endpoint(client):
    response = client.get('/producers/intervals')
    assert response.status_code == 200
    data = response.get_json()
    assert "min" in data
    assert "max" in data
