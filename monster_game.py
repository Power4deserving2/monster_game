import random
from player_auth import create_player, login_player
from battle_engine import create_battle, execute_turn, check_battle_end
from collection import get_player_collection

def main():
    current_player = None

    while True:
        print("\n🎮 Monster Collector CLI")
        print("1. Create Player")
        print("2. Login")
        print("3. Start Wild Battle")
        print("4. View Monster Collection")
        print("5. Level Up a Monster")
        print("7. Propose Trade")
        print("8. Explore and Catch a Monster")
        print("9. Exit")

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

            print(f"🌲 You encountered a wild Rockgrinder!")

            # Mock stats
            player_monster = {
                "name": "Flamewyrm",
                "Attack": 15,
                "Defense": 5
            }
            wild_monster = {
                "name": "Rockgrinder",
                "Attack": 10,
                "Defense": 6
            }

            battle_data = {
                "player1": [player_monster["name"]],
                "player2": [wild_monster["name"]]
            }

            # Start battle
            battle = create_battle(player1_id=current_player.id, monster_teams=battle_data, battle_type="wild")
            battle_id = battle.id

            turn = 1
            while True:
                print(f"\n📦 Turn {turn}")
                print("Choose your move:")
                print("1. Fire Blast (Power 20)")
                print("2. Tackle (Power 10)")
                move = input("> ")

                move_power = 20 if move == '1' else 10
                execute_turn(
                    battle_id,
                    attacker=player_monster,
                    defender=wild_monster,
                    move_power=move_power,
                    attacker_type="Fire",
                    defender_type="Rock"
                )

                print("👾 Wild Rockgrinder attacks back!")
                wild_power = random.choice([8, 12])
                execute_turn(
                    battle_id,
                    attacker=wild_monster,
                    defender=player_monster,
                    move_power=wild_power,
                    attacker_type="Rock",
                    defender_type="Fire"
                )

                if check_battle_end(battle_id):
                    print("🏆 Battle finished!")
                    break

                turn += 1

        elif choice == '4':
            if not current_player:
                print("⚠️ Login first.")
                continue

            collection = get_player_collection(current_player.id)

            if not collection:
                print("📭 You have no monsters yet!")
            else:
                print("📦 Your Monsters:")
                for mon in collection:
                    print(f"- {mon['nickname']} (Lv.{mon['level']}) | Type: {mon['type']} | Rarity: {mon['rarity']}")

        elif choice == '5':
            if not current_player:
                print("⚠️ Login first.")
                continue

            collection = get_player_collection(current_player.id)
            if not collection:
                print("📭 You have no monsters to level up.")
                continue

            print("Which monster do you want to level up?")
            for idx, mon in enumerate(collection):
                print(f"{idx + 1}. {mon['nickname']} (Lv.{mon['level']})")

            sel = input("Enter number: ").strip()
            try:
                sel_idx = int(sel) - 1
                if sel_idx < 0 or sel_idx >= len(collection):
                    raise ValueError()
                # For now, assume monster IDs = index + 1
                from collection import level_up_monster
                level_up_monster(monster_id=sel_idx + 1)
            except:
                print("❌ Invalid choice.")

                else:
                    print("❌ Invalid input.")

        elif choice == '7':
            if not current_player:
                print("⚠️ Login first.")
                continue

            try:
                from trading import propose_trade
                to_player = int(input("Enter ID of player to trade with: "))
                offered = input("Enter ID(s) of your monsters to offer (comma-separated): ").split(",")
                requested = input("Enter ID(s) of their monsters you want: ").split(",")

                offered_ids = [int(mid.strip()) for mid in offered if mid.strip().isdigit()]
                requested_ids = [int(mid.strip()) for mid in requested if mid.strip().isdigit()]

                propose_trade(
                    from_player=current_player.id,
                    to_player=to_player,
                    offered_monsters=offered_ids,
                    requested_monsters=requested_ids
                )

            except Exception as e:
                print("❌ Trade failed. Check input.")

        elif choice == '8':
            if not current_player:
                print("⚠️ Login first.")
                continue

            from catching import catch_monster
            # You can simulate wild encounter with a random ID (say 1 to 3)
            species_id = random.choice([1, 2, 3])
            catch_monster(current_player.id, species_id)

if __name__ == "__main__":
    main()