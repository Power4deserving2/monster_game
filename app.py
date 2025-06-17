from sqlalchemy import create_engine
from base import Base
from models.players import Player
from models.Battles import Battle
from models.players_monsters import PlayerMonster
from models.monster_species import MonsterSpecies

if __name__ =="__main__":
    engine =create_engine("sqlite:///Tables/monster.db")
    Base.metadata.create_all(engine)

