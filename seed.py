from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
# from models.players import Player
from models.monster_species import MonsterSpecies

\
engine = create_engine("sqlite:///Tables/monster.db")
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)


# player = Player(
#     username="YasirHero",
#     level=1,
#     experience=0
# )

# Seed monster species
monsters = [
    MonsterSpecies(
        name="Flamewyrm",
        power_type="Fire",
        starting_stats={"health": 100, "Attack": 70, "Defence": 40, "Speed": 12},
        strengths="Air",
        weakness="Water",
        rarity="Rare"
    ),
    MonsterSpecies(
        name="Aquafin",
        power_type="Water",
        starting_stats={"health": 120, "Attack": 50, "Defence": 60, "Speed": 10},
        strengths="Fire",
        weakness="Electric",
        rarity="Common"
    ),
    MonsterSpecies(
        name="Terrachamp",
        power_type="Earth",
        starting_stats={"health": 140, "Attack": 80, "Defence": 70, "Speed": 6},
        strengths="Electric",
        weakness="Air",
        rarity="Uncommon"
    ),
    MonsterSpecies(
        name="Voltbolt",
        power_type="Electric",
        starting_stats={"health": 90, "Attack": 75, "Defence": 40, "Speed": 15},
        strengths="Water",
        weakness="Earth",
        rarity="Rare"
    ),
    MonsterSpecies(
        name="Vinewhip",
        power_type="Grass",
        starting_stats={"health": 100, "Attack": 60, "Defence": 50, "Speed": 9},
        strengths="Water",
        weakness="Fire",
        rarity="Common"
    ),
    MonsterSpecies(
        name="Sandmaw",
        power_type="Earth",
        starting_stats={"health": 130, "Attack": 65, "Defence": 80, "Speed": 5},
        strengths="Electric",
        weakness="Water",
        rarity="Uncommon"
    ),
    MonsterSpecies(
        name="Blazetalon",
        power_type="Fire",
        starting_stats={"health": 95, "Attack": 85, "Defence": 45, "Speed": 13},
        strengths="Grass",
        weakness="Water",
        rarity="Rare"
    ),
    MonsterSpecies(
        name="Glacior",
        power_type="Water",
        starting_stats={"health": 110, "Attack": 55, "Defence": 60, "Speed": 8},
        strengths="Fire",
        weakness="Electric",
        rarity="Common"
    ),
    MonsterSpecies(
        name="Stormling",
        power_type="Air",
        starting_stats={"health": 85, "Attack": 60, "Defence": 40, "Speed": 18},
        strengths="Earth",
        weakness="Electric",
        rarity="Legendary"
    ),
    MonsterSpecies(
        name="Wraithclaw",
        power_type="Dark",
        starting_stats={"health": 100, "Attack": 90, "Defence": 45, "Speed": 14},
        strengths="Psychic",
        weakness="Light",
        rarity="Legendary"
    )
]


# session.add(player)
session.add_all(monsters)
session.commit()


# print(f"Seeded player: {player.username}")
print("Seeded monsters:")
for m in monsters:
    print(f"- {m.name} ({m.power_type}, Rarity: {m.rarity})")
