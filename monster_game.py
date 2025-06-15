from player_auth import create_player, login_player
from battle_engine import create_battle

def main():
    current_player = None

    while True:
        print("\n🎮 Monster Collector CLI")
        print("1. Create Player")
        print("2. Login")
        print("3. Start Wild Battle")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            username = input("Enter new username: ").strip()
            current_player = create_player(username)
        elif choice == '2':
            username = input("Enter username to login: ").strip()
            current_player = login_player(username)
        elif choice == '3':
            if not current_player:
                print("⚠️ You need to login first!")
                continue

            print(f"🌲 Exploring... You encounter a wild Rockgrinder!")
            mock_team = {
                "player1": ["Flamewyrm"],
                "player2": ["Rockgrinder"]
            }
            create_battle(player1_id=current_player.id, monster_teams=mock_team, battle_type="wild")
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input.")

if __name__ == "__main__":
    main()