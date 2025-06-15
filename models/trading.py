from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.trades import Trade

engine = create_engine("sqlite:///Tables/monster.db")
Session = sessionmaker(bind=engine)
session = Session()

def propose_trade(from_player, to_player, offered_monsters, requested_monsters):
    """Create a trade request between two players."""
    trade = Trade(
        from_player=from_player,
        to_player=to_player,
        offered_monsters=offered_monsters,
        requested_monsters=requested_monsters
    )
    session.add(trade)
    session.commit()
    print(f"📦 Trade proposed from Player {from_player} to Player {to_player}")
    return trade