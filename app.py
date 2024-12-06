
"""
app.py
============================
Descrição:
Este módulo implementa funcionalidades de API RESTful para gerenciar uma lista de filmes.

Autores:
Desenvolvido por Julio Cesar da Silva Santos.

Modificações:
Adicionado mais logs e simplificado o carregamento do CSV para garantir que todos os registros sejam carregados.
"""

import logging
from flask import Flask, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
import csv

# Configura logging para depuração
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configura o banco de dados em memória
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    """
    Modelo para armazenar informações sobre os filmes no banco de dados.
    """
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    studios = db.Column(db.String, nullable=False)
    producers = db.Column(db.String, nullable=False)
    winner = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"<Movie {self.title}>"


def load_csv_to_db(csv_path):
    """
    Lê os dados do arquivo CSV e insere no banco de dados.
    
    :param csv_path: Caminho do arquivo CSV.
    """
    logger.info(f"Iniciando carregamento do CSV: {csv_path}")
    count = 0
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            logger.debug(f"Processando linha: {row}")
            try:
                movie = Movie(
                    year=int(row['year']),
                    title=row['title'],
                    studios=row['studios'],
                    producers=row['producers'],
                    winner=row.get('winner', '').strip().lower() == 'yes'
                )
                db.session.add(movie)
                count += 1
            except Exception as e:
                logger.error(f"Erro ao processar linha: {row}. Erro: {e}")
    db.session.commit()
    logger.info(f"Carregamento concluído. Total de registros carregados: {count}")


@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Endpoint para retornar todos os filmes no banco de dados.

    :return: JSON contendo a lista de filmes.
    """
    movies = Movie.query.all()
    result = [
        {
            "id": movie.id,
            "year": movie.year,
            "title": movie.title,
            "studios": movie.studios,
            "producers": movie.producers,
            "winner": movie.winner
        }
        for movie in movies
    ]
    return jsonify(result)


@app.route('/producers/intervals', methods=['GET'])
def get_producer_intervals():
    """
    Endpoint para calcular os produtores com maior e menor intervalo entre prêmios.

    :return: JSON com os resultados.
    """
    movies = Movie.query.filter_by(winner=True).all()
    producer_intervals = {}

    for movie in movies:
        producers = [p.strip() for p in movie.producers.split(',')]
        for producer in producers:
            if producer not in producer_intervals:
                producer_intervals[producer] = []
            producer_intervals[producer].append(movie.year)

    result = []
    for producer, years in producer_intervals.items():
        if len(years) > 1:
            years.sort()
            intervals = [y2 - y1 for y1, y2 in zip(years, years[1:])]
            result.append({
                "producer": producer,
                "min_interval": min(intervals),
                "max_interval": max(intervals),
            })

    return jsonify(result)


@app.route('/')
def index():
    """
    Renderiza a página principal com a lista de filmes formatada.

    :return: HTML da página principal.
    """
    movies = Movie.query.all()
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lista de Filmes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
            }
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #00c8ff;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            h1 {
                text-align: center;
                margin-top: 20px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Lista de Filmes</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Ano</th>
                    <th>Título</th>
                    <th>Vencedor?</th>
                </tr>
            </thead>
            <tbody>
                {% for movie in movies %}
                <tr>
                    <td>{{ movie.id }}</td>
                    <td>{{ movie.year }}</td>
                    <td>{{ movie.title }}</td>
                    <td>{{ 'Sim' if movie.winner else 'Não' }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    return render_template_string(html_template, movies=movies)


if __name__ == '__main__':
    # Inicializa o banco de dados e carrega os dados do CSV dentro do contexto da aplicação
    with app.app_context():
        db.create_all()
        load_csv_to_db('movielist.csv')
    app.run(debug=True)
