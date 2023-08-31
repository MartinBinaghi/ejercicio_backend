from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://root:admin@localhost:3306/ejercicio_backend")   

metadata = MetaData()

conn = engine.connect()