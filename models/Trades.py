from sqlalchemy import Column, Integer, ForeignKey, JSON
from base import Base

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    from_player = Column(Integer, ForeignKey('players.id'), nullable=False)
    to_player = Column(Integer, ForeignKey('players.id'), nullable=False)
    offered_monsters = Column(JSON, nullable=False)
    requested_monsters = Column(JSON, nullable=False)
    status = Column(String, default="pending")  # pending / accepted / declined