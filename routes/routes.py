from fastapi import APIRouter
from sqlalchemy import func, select
from starlette.status import HTTP_204_NO_CONTENT

from models.models import data
from config.db import conn
from schemas.schema import Book

main = APIRouter()

@main.get(
    "/get_data/{id}",
    tags=["data"],
    response_model=Book,
    description="Get a single book by Id",
)
def get_book(id: str):
    return conn.execute(data.select().where(data.c.id == id)).first()

@main.post("/input/{my_target_field}", tags=["data"], response_model=Book)
def modify_text(book: Book, my_target_field: str):
    
    if my_target_field == "field_1":
        modified_text = book.field_1.upper()
        book.field_1 = modified_text
    elif my_target_field == "author":
        modified_text = book.author.upper()
        book.author = modified_text
    elif my_target_field == "description":
        modified_text = book.description.upper()
        book.description = modified_text
    else:
        return {"error": (my_target_field) + " no es un campo válido para convertir a mayúsculas"}

    new_value = {        
        "field_1": book.field_1,
        "author": book.author,
        "description": book.description,
        "my_numeric_field": book.my_numeric_field,
        }
    
    result = conn.execute(data.insert().values(new_value))
    return conn.execute(data.select().where(data.c.id == result.lastrowid)).first()

@main.delete("/delete/{id}", tags=["data"], status_code=HTTP_204_NO_CONTENT)
def delete_book(id: int):
    conn.execute(data.delete().where(data.c.id == id))
    return conn.execute(data.select().where(data.c.id == id)).first()