from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from player_monsters import PlayerMonster
from monster_species import MonsterSpecies

engine = create_engine("sqlite:///Tables/monster.db")
Session = sessionmaker(bind=engine)
session = Session()

def get_player_collection(player_id):
    """Return a list of the player’s monsters and their info."""
    monsters = session.query(PlayerMonster, MonsterSpecies).join(
        MonsterSpecies, PlayerMonster.species_id == MonsterSpecies.id
    ).filter(PlayerMonster.player_id == player_id).all()

    collection = []
    for pm, species in monsters:
        collection.append({
            "nickname": pm.nickname or species.name,
            "level": pm.level,
            "type": species.power_type,
            "rarity": species.rarity
        })
    return collection

def level_up_monster(monster_id):
    """Increase monster level and boost stats."""
    mon = session.query(PlayerMonster).filter_by(id=monster_id).first()

    if not mon:
        print("❌ Monster not found.")
        return None

    mon.level += 1
    if mon.stats:
        mon.stats['Attack'] += 2
        mon.stats['Defense'] += 1
    session.commit()
    print(f"✨ {mon.nickname or 'Monster'} leveled up to Lv.{mon.level}!")
    return mon