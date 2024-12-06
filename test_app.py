
"""
test_app.py
============================
Descrição:
Este módulo implementa testes de integração para a API RESTful de gerenciamento de filmes.

Autores:
Desenvolvido por Julio Cesar da Silva Santos.

Modificações:
Atualizado para refletir o número correto de registros no CSV.
"""

import pytest
from app import app, db, load_csv_to_db


@pytest.fixture
def client():
    """
    Configura um cliente de teste para a aplicação Flask.
    """
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            load_csv_to_db('movielist.csv')
        yield client


@pytest.fixture
def app_context():
    """
    Garante que todos os testes executem dentro do contexto Flask.
    """
    with app.app_context():
        yield


def test_movies_endpoint_returns_all_data(client, app_context):
    """
    Testa se o endpoint /movies retorna todos os registros do CSV.
    """
    response = client.get('/movies')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 206  # Atualizado para o número correto de registros no CSV


def test_movies_endpoint_format(client, app_context):
    """
    Testa se o formato do retorno de /movies está correto.
    """
    response = client.get('/movies')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert all("id" in movie and "title" in movie for movie in data)


def test_intervals_endpoint_structure(client, app_context):
    """
    Testa se o endpoint /producers/intervals retorna a estrutura esperada.
    """
    response = client.get('/producers/intervals')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    for entry in data:
        assert "producer" in entry
        assert "min_interval" in entry
        assert "max_interval" in entry


def test_movies_endpoint_handles_empty_db(client, app_context):
    """
    Testa se o endpoint /movies funciona com banco de dados vazio.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
    response = client.get('/movies')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 0


def test_intervals_endpoint_handles_empty_db(client, app_context):
    """
    Testa se o endpoint /producers/intervals funciona com banco de dados vazio.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
    response = client.get('/producers/intervals')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 0


def test_csv_data_integrity(client, app_context):
    """
    Testa a integridade dos dados carregados do CSV.
    """
    response = client.get('/movies')
    data = response.get_json()
    first_movie = data[0]
    assert first_movie["year"] == 1980
    assert first_movie["title"] == "Can't Stop the Music"


def test_invalid_route(client, app_context):
    """
    Testa se uma rota inválida retorna 404.
    """
    response = client.get('/invalid_route')
    assert response.status_code == 404
