"""
app.py
============================
Descrição:
Este módulo implementa funcionalidades de API RESTful para gerenciar uma lista de filmes.

Autores:
Desenvolvido por Julio Cesar da Silva Santos.

Modificações:
Atualizado com padrões Javadoc, princípios SOLID e Clean Code.
"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configura o banco de dados em memória
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de dados para o banco de dados
class Movie(db.Model):
    """
    Modelo para armazenar informações sobre os filmes no banco de dados.
    """
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    studios = db.Column(db.String, nullable=False)
    producers = db.Column(db.String, nullable=False)
    winner = db.Column(db.Boolean, default=False)

# Função para popular o banco de dados
def populate_database():
    """
    Lê os dados do arquivo CSV e insere no banco de dados.
    """
    import csv
    try:
        with open('movielist.csv', 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                movie = Movie(
                    year=int(row['year']),
                    title=row['title'],
                    studios=row['studios'],
                    producers=row['producers'],
                    winner=row['winner'].strip().lower() == 'yes'
                )
                db.session.add(movie)
            db.session.commit()
    except FileNotFoundError:
        print("Erro: Arquivo 'movielist.csv' não encontrado.")
    except KeyError as e:
        print(f"Erro: Chave ausente no arquivo CSV: {e}")

# Rota para calcular os intervalos dos produtores
@app.route('/producers/intervals', methods=['GET'])
def get_intervals():
    """
    Calcula e retorna os produtores com os menores e maiores intervalos entre prêmios consecutivos.
    """
    winners = Movie.query.filter_by(winner=True).all()
    producers_intervals = {}

    # Processa os intervalos para cada produtor
    for movie in winners:
        for producer in movie.producers.split(','):
            producer = producer.strip()
            if producer not in producers_intervals:
                producers_intervals[producer] = []
            producers_intervals[producer].append(movie.year)

    # Calcula os intervalos mínimo e máximo
    intervals = {"min": [], "max": []}
    for producer, years in producers_intervals.items():
        if len(years) > 1:
            sorted_years = sorted(years)
            min_interval = min(y2 - y1 for y1, y2 in zip(sorted_years, sorted_years[1:]))
            max_interval = max(y2 - y1 for y1, y2 in zip(sorted_years, sorted_years[1:]))
            intervals["min"].append({
                "producer": producer,
                "interval": min_interval,
                "previousWin": sorted_years[0],
                "followingWin": sorted_years[1]
            })
            intervals["max"].append({
                "producer": producer,
                "interval": max_interval,
                "previousWin": sorted_years[0],
                "followingWin": sorted_years[1]
            })

    return jsonify(intervals)

# Inicializa o banco de dados e popula os dados
with app.app_context():
    db.create_all()
    populate_database()

# Rota inicial opcional
@app.route('/', methods=['GET'])
def home():
    """
    Rota inicial da API.
    """
    return "Bem-vindo à API do Golden Raspberry Awards!"

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
