from sqlalchemy import Column, Integer, String, create_engine, MetaData

metadata = MetaData()

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/ejercicio_backend")   

conn = engine.connect()