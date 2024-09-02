import sqlite3
import pandas as pd
from pandas import DataFrame
from jinja2 import Environment, FileSystemLoader


from db_item_a import items

from db_const import db_sqlite_filename as dbfile_name
from db_const import db_type_sqlite     as db_type

import x_utils

from db_const import idx_col_left
from db_const import idx_desc


force_crate = True



# Connect DB
connection = sqlite3.connect(dbfile_name)
str_select = f"SELECT * FROM LEFT LIMIT 5"
df = pd.read_sql_query(str_select, connection)
connection.close()

print(df)

# To CSV
df.to_csv("data_sample/LEFT_PANDAS.csv", index=False, encoding="UTF-8")

# 모두 str로 변환
df = df.astype(str)

# Header 추가
list_header = []
for item in items:
    list_header.append(item[idx_desc])

df.loc[0] = list_header


# 행열 변환
df=df.transpose()

# To HTML
# 템플릿 파일이 있는 디렉토리 설정
file_loader = FileSystemLoader('template_html')
env = Environment(loader=file_loader)

# 템플릿 파일 로드
template = env.get_template('pd_template.html')



# 템플릿 렌더링
output = template.render(dataframe=df)

# 렌더링된 템플릿 출력
# print(output)
str_filename = x_utils.get_date_filename('data_report', 'pd_report', 'html')
with open(str_filename, 'w', encoding="UTF-8") as f:
    f.writelines(output)
