from typing import List, Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: Optional[int] 
    field_1: str
    author: str
    description: str
    my_numeric_field: int
