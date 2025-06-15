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

TYPE_EFFECTIVENESS = {
    "Fire": {"Grass": 2, "Water": 0.5, "Electric": 1},
    "Water": {"Fire": 2, "Grass": 0.5, "Electric": 0.5},
    "Grass": {"Water": 2, "Fire": 0.5, "Electric": 1},
    "Electric": {"Water": 2, "Grass": 1, "Fire": 1}
}

def calculate_damage(attacker_stats, defender_stats, move_power, attacker_type, defender_type):
    """Basic damage calculation with type effectiveness"""
    effectiveness = TYPE_EFFECTIVENESS.get(attacker_type, {}).get(defender_type, 1)
    base_damage = (attacker_stats['Attack'] - defender_stats['Defense']) + move_power
    damage = max(int(base_damage * effectiveness), 1)  # Ensure min damage = 1
    return damage

def execute_turn(battle_id, attacker, defender, move_power, attacker_type, defender_type):
    """Run one turn and update the battle record (simplified)"""
    damage = calculate_damage(attacker, defender, move_power, attacker_type, defender_type)

    # Log it to the result field (we'll keep it as a simple JSON array for now)
    session = Session()
    battle = session.query(Battle).filter_by(id=battle_id).first()

    if not battle.result:
        battle.result = []

    log_entry = {
        "attacker": attacker['name'],
        "defender": defender['name'],
        "damage": damage,
        "move_power": move_power,
        "attacker_type": attacker_type,
        "defender_type": defender_type
    }

    battle.result.append(log_entry)
    session.commit()

    print(f"💥 {attacker['name']} dealt {damage} damage to {defender['name']}")
    return log_entry