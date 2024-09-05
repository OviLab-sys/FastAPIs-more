import sqlite3
from model.creature import Creature

DB_NAME = "cryptid.db"
conn =sqlite3.connect(DB_NAME)
curs = conn.cursor()

def init():
    curs.execute("create table creature(name,description, country, area, aka)")

def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)

def model_to_dict(creature: Creature) ->dict:
    return creature.model_dump()

def get_one(name:str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)