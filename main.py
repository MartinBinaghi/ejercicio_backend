from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

"""DATABASE_URL = "mysql://root:admin@db:3306/ejercicio_backend"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()"""

"""class ModifiedData(Base):
    __tablename__ = "modified_data"
    
    field_1: Column(String)
    author: Column(String)
    description: Column(String)
    my_numeric_field: Column(Integer)"""

"""@app.post("/input/{my_target_field}")
async def modify_text(my_target_field: str, data: dict):
    valid_fields = ["field_1", "author", "description"]
    if my_target_field not in valid_fields:
        return {"error": (my_target_field) + "no es un campo válido para convertir a mayúsculas"}

    modified_text = data[my_target_field].upper()
    data[my_target_field] = modified_text


    db = SessionLocal()
    db_data = ModifiedData(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    db.close()
    return db_data"""


""" @app.get("/get_data/{id}", response_model=ModifiedData)
async def get_data(id: int):
    db = SessionLocal()
    data = db.query(ModifiedData).filter(ModifiedData.id == id).first()
    db.close()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data"""
    
    





