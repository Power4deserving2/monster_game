from sqlalchemy import Column,Integer,ForeignKey
from base import Base


class PlayerMonster(Base):
     __tablename__ ="player_monsters"


     id = Column(Integer, primary_key=True)
     player_id = Column(Integer ,ForeignKey("player.id"))
     monster_species_id = Column(Integer,ForeignKey("monster_species.id"))
     level = Column(Integer, default =1)
     current_health = Column(Integer,default=100)
     


