from .init import conn, curs
import sqlite3
from model.creature import Creature

DB_NAME = "cryptid.db"
curs = conn.cursor()

curs.execute("""create table if not exists creature(name text, 
             primary key, 
             description text, 
             country text,
             area text, 
             aka text)""")


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

def get_all(name:str) -> list[Creature]:
    qry ='select * from creature'
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row)for row in rows]

def create(creature: Creature):
    qry = "insert into creature values (:name, :description, :country, :area, :aka)"
    params = model_to_dict(creature)
    curs.execute(qry,params)

def modify(creature: Creature) ->Creature:
    qry ="""update creature set country=:country, 
            name=:name,
            description=:description,
            area=:area,
            aka=:aka 
            where name=: name_origi""" 
    params = model_to_dict(creature)
    params["name_origi"]
    _= curs.execute(qry,params)
    return get_one(creature.name)

def delete(creature: Creature):
    qry = "delete from creature where name =:name"
    params = {"name":creature.name}
    res = curs.execute(qry,params)
    return bool(res)