from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.players import Player

# Set up engine and session
engine = create_engine("sqlite:///Tables/monster.db")
Session = sessionmaker(bind=engine)
session = Session()

def create_player(username):
    """Create a new player with default stats."""
    existing = session.query(Player).filter_by(username=username).first()
    if existing:
        print(f"❌ Player with username '{username}' already exists.")
        return None
    
    new_player = Player(username=username)
    session.add(new_player)
    session.commit()
    print(f"✅ Player '{username}' created successfully!")
    return new_player

def login_player(username):
    """Log in an existing player by username."""
    player = session.query(Player).filter_by(username=username).first()
    if player:
        print(f"🔓 Welcome back, {player.username}!")
        return player
    else:
        print(f"❌ No player found with username '{username}'.")
        return None