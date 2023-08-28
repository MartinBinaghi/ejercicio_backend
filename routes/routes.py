from fastapi import APIRouter, HTTPException
from config.db import conn
from models.models import book
from schemas.schema import Book

main = APIRouter()

@main.get("/get_data/{id}")
async def get_data(id: int):
    query = book.select().where(book.c.id == id)
    return conn.execute(query).fetchone()

@main.post("/input/{my_target_field}")
async def modify_text(book: Book, my_target_field: str, data: dict):
    
    valid_fields = ["field_1", "author", "description"]
    if my_target_field not in valid_fields:
        return {"error": (my_target_field) + " no es un campo válido para convertir a mayúsculas"}
    
    modified_text = data[my_target_field].upper()
    data[my_target_field] = modified_text

    query = book.insert().values(
        field_1 = data["field_1"],
        author = data["author"],
        description = data["description"],
        my_numeric_field = data["my_numeric_field"]
    )

    conn.execute(query)
    return conn.execute("SELECT * FROM book ORDER BY id DESC LIMIT 1").fetchone()