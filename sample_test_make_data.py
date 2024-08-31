import random
from uuid_extensions import uuid7, uuid7str

from db_const import idx_idx            
from db_const import idx_desc           
from db_const import idx_col_left       
from db_const import idx_col_right      
from db_const import idx_type           

from db_const import table_name_left   
from db_const import table_name_right  
from db_const import table_name_result 

from db_item_a import items

def make_data(cursor):
    # init col
    str_col_left   = ""
    str_col_right  = ""
    str_col_result = ""

    str_val_left   = ""
    str_val_right  = ""
    str_val_result = ""

    idx = 0
    for item in items:
        idx += 1
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

        str_val_left   += f":{idx}"
        str_val_right  += f":{idx}"
        str_val_result += f":{idx}"
    # End of For

    # Insert Sql
    str_insert_left   = f"insert into {table_name_left}   ({str_col_left})   values ({str_val_left})"
    str_insert_right  = f"insert into {table_name_right}  ({str_col_right})  values ({str_val_right})"
    str_insert_result = f"insert into {table_name_result} ({str_col_result}) values ({str_val_result})"

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
                data.append(round(random.uniform(0.0, 1000000.0), 2))
        # End of For

        # Insert
        # print(str_insert_left)
        # print(data)
        cursor.execute(str_insert_left, data)

        if i % 10000 == 0:
            print(f'{format(i,",d").rjust(10)} records processed')

    # End of For
