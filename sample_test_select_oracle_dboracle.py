
from db_engin import db 

import oracledb

import sample_test_make_data
from db_item_a import items

from db_const import db_type_oracle     as db_type
from db_const import db_oracle_user
from db_const import db_oracle_pass
from db_const import db_oracle_conn

import pandas as pd


force_crate = True

# Connect DB
connection = oracledb.connect(user=db_oracle_user, password=db_oracle_pass, dsn=db_oracle_conn)


str_sql_select = f"SELECT * FROM LEFT"


# cursor = connection.cursor()     
# cursor.execute(str_sql_select,)
# for row in cursor:
#     print(row)


df = pd.read_sql_query(str_sql_select, connection)
print(df)

connection.commit()
connection.close()