from flask import Flask
from sqlalchemy import create_engine
from json import loads, dumps
import psycopg2
import pandas as pd
import datetime

app = Flask(__name__)
engine = create_engine("postgresql://mstr:Be3F7R82FphU@localhost:5432/pagila")
sql_film_list_df = pd.read_sql("SELECT * FROM film_list UNION SELECT * from nicer_but_slower_film_list", con=engine)
sql_sales_by_category_df = pd.read_sql("SELECT * FROM sales_by_film_category", con=engine)
sql_sales_by_store_df = pd.read_sql("SELECT * FROM sales_by_store", con=engine)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/getdate")
def date():
    return {
        "sysdate": datetime.datetime.now()
    }

@app.route("/getfilmlist")
def getting_film_list():
    result = sql_film_list_df.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed)

@app.route("/getsalescategory")
def get_sales_category():
    result = sql_sales_by_category_df.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed)

@app.route("/getsalesstore")
def get_sales_store():
    result = sql_sales_by_store_df.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed)