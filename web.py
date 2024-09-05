from model.model import Creature
from fastapi import FastAPI
from data import get_creatures

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    return get_creatures()