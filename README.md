# API RESTful - Golden Raspberry Awards

## Descrição
API que retorna os produtores com os maiores e menores intervalos entre prêmios consecutivos.

## Pré-requisitos
- Python 3.7 ou superior
- Pip (gerenciador de pacotes)

## Instalação
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install flask flask_sqlalchemy pytest
   ```

## Executando a API
1. Execute o arquivo `app.py`:
   ```bash
   python app.py
   ```
2. Acesse o endpoint:
   ```bash
   http://127.0.0.1:5000/producers/intervals
   ```

## Executando os testes
1. Execute o comando:
   ```bash
   pytest
   ```

## Estrutura do Projeto
- `app.py`: Código principal da aplicação.
- `movielist.csv`: Arquivo de entrada com os dados dos filmes.
- `README.md`: Instruções para executar o projeto.


## Como rodar o projeto

1. Certifique-se de ter Python 3 instalado.
2. Instale as dependências executando:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicie o projeto:
   ```bash
   python app.py
   ```

## Como executar os testes

1. Execute os testes com o comando:
   ```bash
   pytest test_app.py
   ```


## Como rodar o projeto

### Pré-requisitos
- Python 3.8 ou superior.
- Virtualenv (opcional, mas recomendado).

### Passos para executar o projeto
1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd API_RESTful
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate   # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o servidor da API:
   ```bash
   python app.py
   ```

6. Acesse a API em `http://localhost:5000`.

## Como executar os testes
1. Certifique-se de que o ambiente virtual (se criado) está ativo.
2. Execute os testes com:
   ```bash
   pytest test_app.py
   ```

### Notas adicionais
- A base de dados é criada automaticamente na memória ao iniciar a aplicação.
- O arquivo CSV `movielist.csv` deve estar no mesmo diretório que `app.py`.
