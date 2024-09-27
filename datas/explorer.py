from .init import (curs,conn,IntegrityError)
from model.explorer import Explorer
from errors import Missing,Duplicate

curs.execute(
    """create table if not exists explorer(name text primary key,
    country text, description text)
""")

def row_to_model(row: tuple) ->Explorer:
    return Explorer(name=row[0],country=row[1], description=row[2])

def model_to_dict(explorer:Explorer) -> dict:
    return explorer.dump_model() if explorer else None

def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Explorer{name} not found")

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(explorer: Explorer) -> Explorer:
    if not explorer: 
        return None
    qry = """insert into explorer (name, country, description)
            values (:name, :country, :description)"""
    params = model_to_dict(explorer)
    try:
        _ = curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg= f"Explorer {explorer.name} alreday exists")
    return get_one(explorer.name)

def modify(name: str, explorer: Explorer) -> Explorer:
    if not (name and explorer): 
        return None
    qry = """update explorer
            set country=:country,
            name=:name,
            description=:description
            where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(msg=f"Explorer [name] not found")

def delete(name: str):
    if not name:
        return False
    qry = "delete from explorer where name = :name"
    params = {"name":name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Explorer {name} not found")