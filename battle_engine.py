from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.battles import Battle

engine = create_engine("sqlite:///Tables/monster.db")
Session = sessionmaker(bind=engine)
session = Session()

def create_battle(player1_id, player2_id=None, monster_teams=None, battle_type="wild"):
    """
    Creates a new battle instance.
    - PvP: player2_id is required
    - Wild: player2_id is None
    """
    if not monster_teams:
        print("⚠️ No monster teams provided.")
        return None

    battle = Battle(
        player1_id=player1_id,
        player2_id=player2_id,
        battle_type=battle_type,
        monster_teams=monster_teams
    )

    session.add(battle)
    session.commit()
    print(f"✅ Battle created with ID: {battle.id}")
    return battle