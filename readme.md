# 🐉 Monster Collector CLI Game

A turn-based text-based monster catching and battling game inspired by Pokémon — built with Python, SQLite, and SQLAlchemy. Players can catch monsters, train them, battle wild foes or other players, and trade monsters to build their ultimate team.

---

## 🎮 Gameplay Features

* 👤 Player creation and login system
* 🌲 Monster exploration with rarity-based catch mechanics
* 📆 Monster collection viewing and management
* ⚔️ Turn-based battle system with type effectiveness
* 🧬 Monster leveling and stat progression
* 🔁 Player-to-player monster trading system
* 📂 Persistent game state via SQLite + SQLAlchemy ORM

---

## 📂 Tech Stack

| Component   | Stack                     |
| ----------- | ------------------------- |
| Language    | Python 3                  |
| DB          | SQLite                    |
| ORM         | SQLAlchemy                |
| CLI Runtime | pipenv (virtualenv)       |
| Styling     | `rich` (optional) for CLI |
| Structure   | Modular Python files      |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your_username>/monster_game.git
cd monster_game
```

### 2. Install Dependencies

```bash
pipenv install
```

### 3. Set Up the Database

```bash
pipenv run python app.py
```

(Optionally seed monsters:)

```bash
pipenv run python seed.py
```

### 4. Start the Game

```bash
pipenv run python monster_game.py
```

---

## 🔑 Core Commands (CLI Options)

| Option | Description                            |
| ------ | -------------------------------------- |
| 1      | Create a new player account            |
| 2      | Log in as an existing player           |
| 3      | Start a wild monster battle            |
| 4      | View your monster collection           |
| 5      | Level up a monster                     |
| 6      | Propose a trade to another player      |
| 7      | Explore and attempt to catch a monster |
| 8      | Exit the game                          |

---

## 🧪 Demo Script

You can follow this flow to demonstrate the full functionality:

1. **Create 2 Players** (Simba and Yasir)
2. **Catch at least 3 monsters**
3. **Battle a wild monster** and win or lose
4. **View monster collection**
5. **Level up a monster**
6. **Propose a trade between two players**
7. **Show persistent save state and rerun**

---

## ✅ Checklist

* [x] SQLAlchemy ORM with relational tables
* [x] Modular CLI with battle, collection, and trade systems
* [x] Input validation and session persistence
* [x] Ready for grading against spec rubric

---

## 🤝 Contributors

* **Simba** – Player, battle, trade, and CLI systems
* **Yasir** – Monster data, models, database foundation

---

## 📄 License

This project is released under the MIT License.

---

> Good luck, monster trainers! 🐲⚡️🌿
