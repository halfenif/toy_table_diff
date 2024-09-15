import random
import secrets
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

from faker import Faker

def make_data(cursor):

    fake = Faker()


    group_list = []
    group_lengh = 10
    
    for i in range(1,group_lengh +1):
        group_list.append(uuid7str())
    

    # init col
    str_col_left   = ""
    str_col_right  = ""

    str_val_left   = ""
    str_val_right  = ""

    idx = 0
    for item in items:
        idx += 1
        if str_col_left:
            str_col_left   += ","
            str_col_right  += ","

            str_val_left     += ","
            str_val_right    += ","

        str_col_left   += f"{item[idx_col_left]}"
        str_col_right  += f"{item[idx_col_right]}"

        str_val_left   += f":{idx}"
        str_val_right  += f":{idx}"
    # End of For

    # Group ID
    str_col_left   += f",col_group_id"
    str_col_right  += f",col_group_id"

    str_val_left   += f",:col_group_id"
    str_val_right  += f",:col_group_id"

    # Insert Sql
    str_insert_left   = f"insert into {table_name_left}   ({str_col_left})   values ({str_val_left})  "
    str_insert_right  = f"insert into {table_name_right}  ({str_col_right})  values ({str_val_right}) "

    # print(str_insert_left)

    data_count = 100 #100만건
    data_origin = []
    data_modify = []

    for i in range(data_count):

        if i > 0 and i % 10000 == 0:
            print(f'{format(i,",d").rjust(10)} records processed')

        target = random.choice(["Left", "Right", "Both"])

        data_origin.clear()
        data_modify.clear()

        for item in items:
            if item[idx_type] == "k":
                str_data = uuid7str()
                data_origin.append(str_data)
                data_modify.append(str_data)
            elif str(item[idx_type]).startswith("s"):

                if item[idx_type] == "s_name":
                    str_data = fake.name().replace("\n"," ")
                elif item[idx_type] == "s_address":
                    str_data = fake.address().replace("\n"," ")
                else:
                    str_data = uuid7str()
                data_origin.append(str_data)
                if random.choice([True, False]):
                    str_data = uuid7str()
                data_modify.append(str_data)
            elif item[idx_type] == "i":
                int_data = secrets.randbits(10)
                data_origin.append(int_data)
                if random.choice([True, False]):
                    int_data = secrets.randbits(10)
                data_modify.append(int_data)
            elif item[idx_type] == "r":
                real_data = round(random.uniform(0.0, 1000000.0), 2)
                data_origin.append(real_data)
                if random.choice([True, False]):
                    real_data = round(random.uniform(0.0, 1000000.0), 2)
                data_modify.append(real_data)
        # End of For

        i_group_id_idx = random.randint(0,group_lengh-1)
        # print(i_group_id_idx)
        str_group_id = group_list[i_group_id_idx]
        data_origin.append(str_group_id)
        data_modify.append(str_group_id)


        # print(str_insert_left)

        choice = random.choice(['L','R','B'])
        if choice == 'L':
            cursor.execute(str_insert_left,  data_origin)
        elif choice == 'R':
            cursor.execute(str_insert_right, data_origin)
        else:
            cursor.execute(str_insert_left,  data_origin)
            cursor.execute(str_insert_right, data_modify)


    # End of For
