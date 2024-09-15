from db_const import db_type_oracle     as db_type
from db_const import db_oracle_user
from db_const import db_oracle_pass
from db_const import db_oracle_conn

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.sql import text
db_engine = create_engine(f"oracle+oracledb://{db_oracle_user}:{db_oracle_pass}@{db_oracle_conn}")

connection = db_engine.connect()

str_sql_select = f"SELECT * FROM LEFT"

# Sqlalchemy
# statement = text(str_sql_select)
# rs = connection.execute(statement,)

# for row in rs:
#     print(row)

#Pandas
df = pd.read_sql_query(str_sql_select, connection)
print(df)

