# AMEDIGITAL-TESTE

Este é um [desafio](https://github.com/AmeDigital/challenge-back-end-hit) da AmeDigital para desenvolver uma api que contenha os dados dos planetas de StarWars como: nome, clima, terreno e a quantidade de aparições em filmes, com as seguintes fucionalidades: adicionar planeta, lista planetas, lista planeta por nome, listar por id e remover planeta.

## Executar
- Crie um ambiente virtual e ative
```
python -m venv venv
source /venv/bin/activate (linux)
/venv/script/activate (windows)
```
- Instale as dependências
```
pip install -r requirements.txt
```
- Execute as migrations para o banco de dados
```
python manage.py migrate
```
- Executar os testes.
```
python manage.py test
```
- Caso também deseje ver a cobertura dos testes, instale a seguinte biblioteca e execute os comandos.
```
pip install coverage
coverage run manage.py test
coverage report
```
- Executar aplicação.
```
python manage.py runserver
```

## Endpoints

```
/api/planets/create - adicionar planeta
/api/planets/list - listar planetas
/api/planets/list?name=nome_do_filme - listar planeta por nome
/api/planets/list/id_do_filme - listar planeta por id
/api/planets/delete/id_do_filme - deletar planeta
```

Documetação dos endpoints: `/docs/` ou `/redoc/`.

## Frameworks e Bibliotecas

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [requests](https://requests.readthedocs.io/)