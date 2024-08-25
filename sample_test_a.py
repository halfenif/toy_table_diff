import db_item_a
from db_engin import db 
import random
from uuid_extensions import uuid7, uuid7str

import sqlite3

from db_const import idx_idx            
from db_const import idx_desc           
from db_const import idx_col_left       
from db_const import idx_col_right      
from db_const import idx_type           

from db_const import table_name_left   
from db_const import table_name_right  
from db_const import table_name_result 



dbfile_name = "sample_item_a.db"
force_crate = True
items = db_item_a.items

# Create Table
db.create_table(dbfile_name, items, force_crate)

# Connect DB
connection = sqlite3.connect(dbfile_name)
cursor = connection.cursor()     

# init col
str_col_left   = ""
str_col_right  = ""
str_col_result = ""

str_val_left   = ""
str_val_right  = ""
str_val_result = ""

for item in items:
    if str_col_left:
        str_col_left   += ","
        str_col_right  += ","
        str_col_result += ","

        str_val_left     += ","
        str_val_right    += ","
        str_val_result   += ","        

    str_col_left   += f"{item[idx_col_left]}"
    str_col_right  += f"{item[idx_col_right]}"
    str_col_result += f"{item[idx_col_right]}"

    str_val_left   += "?"
    str_val_right  += "?"
    str_val_result += "?"
# End of For

# Insert Sql
str_insert_left   = f"insert into {table_name_left}   ({str_col_left})   values ({str_val_left});"
str_insert_right  = f"insert into {table_name_right}  ({str_col_right})  values ({str_val_right});"
str_insert_result = f"insert into {table_name_result} ({str_col_result}) values ({str_val_result});"

# print(str_insert_left)

data_count = 1000000 #100만건
data = []
for i in range(data_count):
    target = random.choice(["Left", "Right", "Both"])

    data.clear()

    for item in items:
        if item[idx_type] == "k":
            data.append(uuid7str())
        elif item[idx_type] == "s":
            data.append(uuid7str())
        elif item[idx_type] == "i":
            data.append(random.randint(0, 100000))
        elif item[idx_type] == "r":
            data.append(random.uniform(0.0, 1000000.0))
    # End of For

    # Insert
    cursor.execute(str_insert_left, data)

    if i % 10000 == 0:
        print(f'{i} records processed')

# End of For


# Commit
connection.commit()
connection.close()