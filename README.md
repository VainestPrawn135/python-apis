# python-apis
Este proyecto almacena dos archivos python creados en 2 frameworks diferentes. Ambos devuelven información de bases de datos montadas en PostgreSQL se convierten a DataFrames de Pandas y se convierten en json

## hello.py
Este archivo se corre instalando Flask y funciona con el comando flask --app hello run. Es una pequeña API que devuelve info de la base de datos Pagila

## main.py
Este archivo corre con el Framework Fast API y con el comando uvicorn main:app --reload. Es otra pequeña API de ejemplo que devuelve info de la base de datos Chinook
