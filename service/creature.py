from model.creature import Creature

__creatures = [
                Creature(name="Yeti",
                        aka="Abominable Snowman",
                        country="CN",
                        area="Himalayas",
                        description="Hirsute Himalayan"),
                Creature(name="Bigfoot",
                        description="Yeti's Cousin Eddie",
                        country="US",
                        area="*",
                        aka="Sasquatch"),
]

def get_all() ->list[Creature]:
    return __creatures

def get_one(name:str) -> Creature|None:
    for _creature in __creatures:
        if _creature.name==name:
            return _creature
    return None

def create(creature:Creature) -> Creature:
    return creature

def modify(creature:Creature) ->Creature:
    return creature

def replace(creature:Creature) ->Creature:
    return creature

def delete(name:str):
    return None