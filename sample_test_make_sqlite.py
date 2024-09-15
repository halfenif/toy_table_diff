
from db_engin import db 

import sqlite3

import sample_test_make_data
from db_item_a import items
from db_item_a import results

from db_const import db_sqlite_filename as dbfile_name
from db_const import db_type_sqlite     as db_type


force_crate = True



# Connect DB
connection = sqlite3.connect(dbfile_name)

# Create Table
db.create_table(db_type, connection, items, results, force_crate)


cursor = connection.cursor()     

sample_test_make_data.make_data(cursor)

# Commit
connection.commit()
connection.close()