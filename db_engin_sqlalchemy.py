from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.engine import reflection

from db_const import db_type_sqlite
from db_const import db_type_oracle
from db_const import db_type_mariadb

class db:
    @staticmethod
    def create_table(engine):

        metadata = MetaData()

        table_left = Table(
            'left', metadata
            ,Column('col-PK', String(36), primary_key=True)
            ,Column('col-001', Integer())
            ,Column('col-002', Integer())
            ,Column('col-003', Integer())
            ,Column('col-004', Float())
            ,Column('col-005', Float())
            ,Column('col-006', Float())
            ,Column('col-007', String(500))
            ,Column('col-008', String(500))
            ,Column('col-009', String(36))            
        )

        inspector = reflection.Inspector.from_engine(engine)

        if 'left' in inspector.get_table_names():
            # Drop the table
            table_left.drop(engine)        

        metadata.create_all(engine)

        

  