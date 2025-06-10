from sqlalchemy import create_engine
from base import Base

if __name__ =="__main__":
    engine =create_engine("sqlite:///Tables/monster.db")
    Base.metadata.create_all(engine)

