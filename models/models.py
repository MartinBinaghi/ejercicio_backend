from sqlalchemy import Table, Column, Integer, String
from config.db import metadata, engine

data = Table("data", metadata, 
    Column("id", Integer, primary_key=True), 
    Column("field_1", String(255)), 
    Column("author", String(255)), 
    Column("description", String(255)), 
    Column("my_numeric_field", Integer))

metadata.create_all(engine)
