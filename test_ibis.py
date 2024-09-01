import ibis

con = ibis.sqlite.connect("sqlite://test.db")
# con.create_table(
#     "penguins", ibis.examples.penguins.fetch().to_pyarrow(), overwrite=True
# )

left = con.table("LEFT")
# print(left.head())

# print(left.select("col_001_left"))
proj = left.select("col_001_left")

print(ibis.to_sql(proj))