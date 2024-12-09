
# API RESTful - Lista de Filmes

Este projeto implementa uma API RESTful para gerenciar uma lista de filmes, seguindo os padrões de Clean Code, princípios SOLID e maturidade de Richardson (nível 2).

## Requisitos

- Python 3.8+
- Flask
- SQLAlchemy
- pytest

## Configuração e Execução

1. **Clonar o Repositório**  
   Certifique-se de clonar o repositório para seu ambiente local ou GitHub Codespaces.

2. **Instalar Dependências**  
   Execute o comando abaixo para instalar as dependências necessárias:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar a Aplicação**  
   Inicie a aplicação com o seguinte comando:  
   ```bash
   python app.py
   ```

4. **Acessar a API**  
   - **Página da Lista de Filmes no Frontend - Apartir desta é possivel acessar todas as outras**
      `GET http://127.0.0.1:5000`

   - **Listar todos os filmes**:  
     `GET http://127.0.0.1:5000/movies`  

   - **Obter intervalos de produtores (maior e menor)**:  
     `GET http://127.0.0.1:5000/producers/intervals`  

   - **Obter anos com Multiplos vencedores**:  
     `GET http://127.0.0.1:5000/producers/multiplewinners` 

   - **Obter os três maiores Studio vencedores**:  
     `GET http://127.0.0.1:5000/studios/top-three`      

     **Página da Lista de Filmes no Frontend GitHube**:  
   - `GET https://literate-winner-jwj5xwgwvjpcp4gr-5000.app.github.dev/`

   - **Obter anos com Multiplos vencedores GitHube**:  
     `GET https://literate-winner-jwj5xwgwvjpcp4gr-5000.app.github.dev/producers/multiplewinners`

 - **Obter os três maiores Studio vencedores GitHube**:  
     `https://literate-winner-jwj5xwgwvjpcp4gr-5000.app.github.dev/studios/top-three`

   - **Listar todos os filmes GitHube**:  
     `GET https://literate-winner-jwj5xwgwvjpcp4gr-5000.app.github.dev/movies`  

   - **Obter intervalos de produtores (maior e menor) GitHube**:  
     `GET https://literate-winner-jwj5xwgwvjpcp4gr-5000.app.github.dev/producers/intervals`  
'

## Testes de Integração

1. **Executar os Testes**  
   Os testes podem ser executados com o comando:  
   ```bash
   pytest
   ```

2. **Cobertura dos Testes**  
   Foram implementados 20 testes de integração para garantir a qualidade e a funcionalidade da aplicação.

## Compatibilidade com GitHub Codespaces

1. **Configuração Automática**  
   O projeto foi adaptado para rodar em Codespaces. Certifique-se de que o ambiente está configurado com Python 3.8+.

2. **Instalação e Execução**  
   Após iniciar o Codespace, siga os passos para instalar as dependências e rodar a aplicação.

## Informações Adicionais

- O banco de dados é carregado diretamente do arquivo `movielist.csv` ao iniciar a aplicação.
- O banco utiliza SQLite em memória, garantindo facilidade no setup.
- Todos os 267 registros do CSV são carregados na inicialização.

## Frontend

Um frontend básico está em desenvolvimento para exibir a lista de filmes com um design UX/UI. Fique atento às próximas atualizações!
