import os
from model.creature import Creature
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as data
else:
    from ..data import creature as data

def get_all() ->list[Creature]:
    return data.get_all()

def get_one(name) -> C