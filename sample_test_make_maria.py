from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from uuid_extensions import uuid7, uuid7str
from faker import Faker
import secrets
import random

from db_const import db_mariadb_uri
from db_engin_sqlalchemy import db


force_crate = True

fake = Faker()

# Connect DB
engine = create_engine(f'{db_mariadb_uri}')

db.create_table(engine)

metadata = MetaData()

table_left = Table('left', metadata, autoload_with=engine)

with engine.connect() as connection:


    values = []
    

    for idx in range(100):
        row = {}

        row["col-PK"] = uuid7str()
        row["col-001"] = secrets.randbits(10)
        row["col-002"] = secrets.randbits(10)
        row["col-003"] = secrets.randbits(10)
        row["col-004"] = round(random.uniform(0.0, 1000000.0), 2)
        row["col-005"] = round(random.uniform(0.0, 1000000.0), 2)
        row["col-006"] = round(random.uniform(0.0, 1000000.0), 2)
        row["col-007"] = fake.name().replace("\n"," ")
        row["col-008"] = fake.address().replace("\n"," ")
        row["col-009"] = uuid7str()

        values.append(row)

    
    insert_sql = table_left.insert().values(values)

    result =connection.execute(insert_sql)
    connection.commit()

    print(f"Inserted {result.rowcount}")

    # select_query = table_left.select()
    # result = connection.execute(select_query)      

