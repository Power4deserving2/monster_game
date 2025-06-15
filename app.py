from sqlalchemy import create_engine
from base import Base
from models.players import Player

if __name__ =="__main__":
    engine =create_engine("sqlite:///Tables/monster.db")
    Base.metadata.create_all(engine)

