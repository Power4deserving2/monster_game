from models.monster_species import MonsterSpecies
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def seed_data():
    engine = create_engine("sqlite:///Tables/monster.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    monster1 =MonsterSpecies (
        name ="Vampire",
        power_type = "Fire",
        starting_stats= {
            "health":100,
            "Attack":60,
            "Defence":50,
            "Speed":9
        },
        strengths ="Fire",
        rarity= "Legendary",
        weakness = "Water"

    )

    session.add(monster1)
    session.commit()
    print("Monster1",monster1.name,monster1.power_type,monster1.starting_stats,monster1.strengths,monster1.rarity,monster1.weakness)


if __name__ =="__main__":
    seed_data()
