
from db_engin import db 

import oracledb

import sample_test_make_data
from db_item_a import items
from db_item_a import results

from db_const import db_type_oracle     as db_type
from db_const import db_oracle_user
from db_const import db_oracle_pass
from db_const import db_oracle_conn


force_crate = True

# Connect DB
connection = oracledb.connect(user=db_oracle_user, password=db_oracle_pass, dsn=db_oracle_conn)

# Create Table
db.create_table(db_type, connection, items, results, force_crate)


cursor = connection.cursor()     

sample_test_make_data.make_data(cursor)

# Commit
connection.commit()
connection.close()