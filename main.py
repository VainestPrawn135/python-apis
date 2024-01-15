from typing import Union

from fastapi import FastAPI

from sqlalchemy import create_engine
from json import loads, dumps
import psycopg2
import pandas as pd
import datetime

app = FastAPI()
engine = create_engine("postgresql://mstr:Be3F7R82FphU@localhost:5432/chinook")
sql_query = '''select il."InvoiceLineId", i."InvoiceId", concat(c."FirstName", ' ', c."LastName") as Full_Customer_Name, t."Name" , il."UnitPrice", il."Quantity", i."Total"  from "InvoiceLine" il 
inner join "Invoice" i 
on il."InvoiceId" = i."InvoiceId"
inner join "Customer" c 
on i."CustomerId" = c."CustomerId" 
inner join "Track" t 
on il."TrackId" = t."TrackId"'''
sql_df = pd.read_sql(sql_query, con=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getdate")
def getting_current_date():
    return {
        "Current Date": datetime.datetime.now()
    }

@app.get("/getdata")
def getting_data():
    result = sql_df.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed)