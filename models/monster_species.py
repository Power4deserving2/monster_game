from sqlalchemy import Column,Integer,String,JSON
from base import Base

class MonsterSpecies(Base):
    __tablename__ = "monster_species"

    id = Column(Integer,primary_key=True)
    name =Column(String)
    power_type =Column(String)
    starting_stats =Column(JSON)
    strengths =Column(String)
    rarity=Column(String)
    weakness =Column(String)



    
    


    