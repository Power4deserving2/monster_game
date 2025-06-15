import random
from battle_engine import execute_turn, check_battle_end

elif choice == '3':
    if not current_player:
        print("⚠️ You need to login first!")
        continue

    print(f"🌲 You encountered a wild Rockgrinder!")

    # Fake monster stats for now
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

    # Create a new battle
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
        log = execute_turn(
            battle_id,
            attacker=player_monster,
            defender=wild_monster,
            move_power=move_power,
            attacker_type="Fire",
            defender_type="Rock"
        )

        # Simulate enemy counter-attack
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