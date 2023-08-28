from fastapi import FastAPI
from schemas.schema import *
from routes.routes import *
from models.models import *
from config.db import *

app = FastAPI()

app.include_router(main)
    





