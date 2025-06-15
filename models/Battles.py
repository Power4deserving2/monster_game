from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.sql import func
from base import Base

class Battle(Base):
    __tablename__ = 'battles'

    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    player2_id = Column(Integer, ForeignKey('players.id'), nullable=True)  # Null if wild battle
    winner_id = Column(Integer, ForeignKey('players.id'), nullable=True)
    battle_type = Column(String, nullable=False)  # "wild" or "player"
    monster_teams = Column(JSON, nullable=False)  # Dict of monster lists
    result = Column(JSON, nullable=True)  # Damage logs, turns, etc.
    timestamp = Column(DateTime(timezone=True), server_default=func.now())