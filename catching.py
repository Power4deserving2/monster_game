import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.player_monsters import PlayerMonster
from models.monster_species import MonsterSpecies

engine = create_engine("sqlite:///Tables/monster.db")
Session = sessionmaker(bind=engine)
session = Session()

RARITY_BASE_RATES = {
    "Common": 0.9,
    "Uncommon": 0.6,
    "Rare": 0.3,
    "Legendary": 0.1
}

def calculate_catch_rate(species_rarity, player_level):
    base = RARITY_BASE_RATES.get(species_rarity, 0.5)
    bonus = min(player_level * 0.01, 0.2)  # Cap bonus
    return base + bonus

def catch_monster(player_id, species_id):
    species = session.query(MonsterSpecies).filter_by(id=species_id).first()
    if not species:
        print("❌ Invalid species.")
        return False

    player_level = 1  # Replace with actual player level later
    rate = calculate_catch_rate(species.rarity, player_level)
    roll = random.random()

    print(f"🎲 Catch rate: {rate:.2f}, rolled: {roll:.2f}")

    if roll <= rate:
        new_mon = PlayerMonster(
            player_id=player_id,
            species_id=species.id,
            nickname=None,
            level=1,
            stats={"Attack": 10, "Defense": 5}
        )
        session.add(new_mon)
        session.commit()
        print(f"✅ Success! {species.name} joined your team!")
        return True
    else:
        print("❌ It escaped!")
        return False