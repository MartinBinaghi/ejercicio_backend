from fastapi import FastAPI
from routes.routes import main

app = FastAPI()

app.include_router(main)
    





