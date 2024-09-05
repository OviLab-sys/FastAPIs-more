from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

"""thing = Creature('Yeti',
                 'CN',
                 'Himalayas',
                 'Hirsute Himalayan',
                 'Abominable Snowman')

print('my name is ',thing.name)"""