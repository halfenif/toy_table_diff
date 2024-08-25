import sqlite3

from db_const import idx_idx            
from db_const import idx_desc           
from db_const import idx_col_left       
from db_const import idx_col_right      
from db_const import idx_type           

from db_const import table_name_left   
from db_const import table_name_right  
from db_const import table_name_result 

class db:
    @staticmethod
    def create_table(dbfile_name, items, force_crate):
        str_table_left   = f"create table {table_name_left}   ("
        str_table_right  = f"create table {table_name_right}  ("
        str_table_result = f"create table {table_name_result} ("

        str_col_left   = ""
        str_col_right  = ""
        str_col_result = ""

        for item in items:
            if str_col_left:
                str_table_left   += ","
                str_table_right  += ","
                str_table_result += ","

            if item[idx_type] == "k":
                str_col_left   = f"{item[idx_col_left] } TEXT PRIMARY KEY"
                str_col_right  = f"{item[idx_col_right]} TEXT PRIMARY KEY"
                str_col_result = f"{item[idx_col_right]}  TEXT PRIMARY KEY"
            elif item[idx_type] == "s":
                str_col_left   = f"{item[idx_col_left] } TEXT"
                str_col_right  = f"{item[idx_col_right]} TEXT"
                str_col_result = f"{item[idx_col_right]}  TEXT"
            elif item[idx_type] == "i":
                str_col_left   = f"{item[idx_col_left] } INT"
                str_col_right  = f"{item[idx_col_right]} INT"
                str_col_result = f"{item[idx_col_right]} INT"
            elif item[idx_type] == "r":
                str_col_left   = f"{item[idx_col_left] } REAL"
                str_col_right  = f"{item[idx_col_right]} REAL"
                str_col_result = f"{item[idx_col_right]} REAL"
            
            str_table_left   += str_col_left
            str_table_right  += str_col_right
            str_table_result += str_col_result
        # End of For

        str_table_left   += ")"
        str_table_right  += ")"
        str_table_result += ")"

        # print(str_table_left)
        # print(str_table_right)

        # Connect DB
        connection = sqlite3.connect(dbfile_name)
        cursor = connection.cursor()     

        # force_crate check
        if force_crate:
            str_table_check = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"

            cursor.execute(str_table_check, (table_name_left,))
            table_exists = cursor.fetchone()
            if table_exists:
                cursor.execute(f"drop table {table_name_left}")

            cursor.execute(str_table_check, (table_name_right,))
            table_exists = cursor.fetchone()
            if table_exists:
                cursor.execute(f"drop table {table_name_right}")                

            cursor.execute(str_table_check, (table_name_result,))
            table_exists = cursor.fetchone()
            if table_exists:
                cursor.execute(f"drop table {table_name_result}")                

        # create table

        cursor.execute(str_table_left)
        cursor.execute(str_table_right)
        cursor.execute(str_table_result)
        connection.commit()
        connection.close()

        print("Table Created")

