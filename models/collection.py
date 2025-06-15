from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.player_monsters import PlayerMonster
from models.monster_species import MonsterSpecies

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