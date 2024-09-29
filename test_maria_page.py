from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

# Setup database connection using SQLAlchemy
from db_const import db_mariadb_uri

engine = create_engine(f'{db_mariadb_uri}')
Session = sessionmaker(bind=engine)
session = Session()

# Define the table you are querying (or use ORM if you have a model class)
metadata = MetaData()
table = Table('left', metadata, autoload_with=engine)

# Function to fetch paginated results
def fetch_page(table, page_size, page_number):
    offset = (page_number - 1) * page_size  # Calculate offset based on the page number
    query = table.select().limit(page_size).offset(offset)
    result = session.execute(query)
    return result.fetchall()

# Main function to handle pagination
def paginate_sqlalchemy(table, page_size):
    page_number = 1
    while True:
        print(f"Fetching page {page_number}")
        records = fetch_page(table, page_size, page_number)

        if not records:
            print("No more records to fetch.")
            break

        for record in records:
            print(record)  # Convert row to dictionary for readable output

        page_number += 1

# Usage
if __name__ == "__main__":
    paginate_sqlalchemy(table, 10)  # Fetch 10 records per page
