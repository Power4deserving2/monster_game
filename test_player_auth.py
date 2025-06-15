from player_auth import create_player, login_player

def main():
    print("🎮 Monster Game - Player Auth Test")
    while True:
        print("\n1. Create Player")
        print("2. Login Player")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username to create: ").strip()
            create_player(username)
        elif choice == '2':
            username = input("Enter your username to login: ").strip()
            login_player(username)
        elif choice == '3':
            print("👋 Bye!")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == "__main__":
    main()