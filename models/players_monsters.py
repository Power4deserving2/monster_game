from sqlalchemy import Column, Integer, ForeignKey, JSON, String
from base import Base

class PlayerMonster(Base):
    __tablename__ = 'player_monsters'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    species_id = Column(Integer, ForeignKey('monster_species.id'), nullable=False)
    nickname = Column(String, nullable=True)
    level = Column(Integer, default=1)
    stats = Column(JSON)  # Actual HP, Attack, etc.