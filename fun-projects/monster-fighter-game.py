#!/bin/python3

import random

def print_title():
    print(r"""
     __  __  ___  _   _ ____ _____ _____ ____  
    |  \/  |/ _ \| \ | / ___|_   _| ____|  _ \
    | |\/| | | | |  \| \___ \ | | |  _| | |_) |
    | |  | | |_| | |\  |___) || | | |___|  _ <
    |_|  |_|\___/|_| \_|____/ |_| |_____|_| \_|
                                                            
     ____ ___  ____  _   _ _____ _____ ____  
    |  __|_ _|/ ___|| | | |_   _| ____|  _ \
    | |_  | || |  _ | |_| | | | |  _| | |_) |
    |  _| | || |_| ||  _  | | | | |___|  _ <
    |_|  |___|\____||_| |_| |_| |_____|_| \_|

    """)

def start_game():
    """
    Main function for the game
    "While: True" will loop until the game ends
    """
    print("Welcome to...")

    print_title()

    player = {
        "gold": random.randint(50, 100),
        "weapon_name": "stick",
        "weapon_damage": 1,
        "inventory": ["stick"]
    }

    print(f"You start with {player['gold']} gold coins.")
    print(f"Your only weapon is a simple {player['weapon_name']} that does {player['weapon_damage']}x damage of your roll.")
    print("You can buy better weapons from the shop as you win gold from defeating monsters.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Fight a monster")
        print("2. Shop")
        print("3. Change equipment")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            fight_monster(player)
        elif choice == "2":
            shop(player)
        elif choice == "3":
            change_equipment(player)
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def fight_monster(player):
    """
    Generate a monster of random strength and compare against player attack roll multiplied by weapon
    """
    monster = generate_monster()
    print(f"A {monster['name']} appears with strength {monster['health']}!")

    input("Press Enter to roll for attack...")

    base_attack = random.randint(1, 20)
    player_attack = int(base_attack * player["weapon_damage"])
    print(f"You roll a base attack of {base_attack}. With your {player['weapon_name']}, your attack is {player_attack}!")

    if player_attack >= monster['health']:
        reward = random.randint(10, 30)
        player["gold"] += reward
        print(f"You defeated the monster! You earn {reward} gold coins.")
    else:
        penalty = random.randint(5, 15)
        player["gold"] -= penalty
        print(f"The monster defeated you! You lose {penalty} gold coins.")

    print(f"Current gold: {player['gold']}")

def generate_monster():
    """
    Generates a set of monster attributes
    """
    monster_names = ["Goblin", "Troll", "Dragon"]
    name = random.choice(monster_names)
    health = random.randint(5, 20)
    attack = random.randint(5, 20)
    return {"name": name, "health": health, "attack":attack}

def shop(player):
    """
    Allow the player to purchase weapons with gold
    """
    weapons = get_all_weapons()

    print("Welcome to the shop!")
    print(f"Your current weapon is a {player['weapon_name']} with {player['weapon_damage']}x damage.")
    print(f"Current gold: {player['gold']}")

    # Filter out weapons the player already owns
    available_weapons = [w for w in weapons if w["name"] not in player.get("inventory", [])]

    if not available_weapons:
        print("You already own all available weapons!")
        return

    for i, weapon in enumerate(available_weapons, start=1):
        print(f"{i}. Buy a {weapon['name']} for {weapon['damage']}x damage ({weapon['cost']} gold)")

    print(f"{len(available_weapons) + 1}. Leave the shop")

    choice = input("Enter your choice: ").strip()

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(available_weapons):
            selected = available_weapons[choice - 1]
            if player["gold"] >= selected["cost"]:
                player["gold"] -= selected["cost"]
                player["weapon_name"] = selected["name"]
                player["weapon_damage"] = selected["damage"]
                player.setdefault("inventory", []).append(selected["name"])
                print(f"You bought a {selected['name']}!")
            else:
                print("You don't have enough gold!")
        else:
            print("You leave the shop.")
    else:
        print("Invalid input. You leave the shop.")

    print(f"Current gold: {player['gold']}")

def change_equipment(player):
    """
    Allows the player to change which weapon is equipped.
    """
    if "inventory" not in player or len(player["inventory"]) == 0:
        print("You have no weapons in your inventory.")
        return

    print("\nYour Inventory:")
    for i, weapon_name in enumerate(player["inventory"], start=1):
        # Get the weapon details from a central list (same as in shop)
        weapon = next((w for w in get_all_weapons() if w["name"] == weapon_name), None)
        if weapon:
            print(f"{i}. {weapon['name']} ({weapon['damage']}x damage)")

    choice = input("Enter the number of the weapon you want to equip: ").strip()

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(player["inventory"]):
            selected_name = player["inventory"][choice - 1]
            weapon = next(w for w in get_all_weapons() if w["name"] == selected_name)
            player["weapon_name"] = weapon["name"]
            player["weapon_damage"] = weapon["damage"]
            print(f"You have equipped the {weapon['name']}!")
        else:
            print("Invalid choice.")
    else:
        print("Invalid input.")

def get_all_weapons():
    """
    Set the inventory of all available weapons
    Used by shop and equipment changes
    """
    return [
        {"name": "stick", "damage": 1, "cost": 0},
        {"name": "sword", "damage": 2, "cost": 50},
        {"name": "axe", "damage": 3, "cost": 100},
        {"name": "mace", "damage": 4, "cost": 200},
        {"name": "magic staff", "damage": 5, "cost": 300},
        {"name": "rubber ducky of doom", "damage": 6, "cost": 500}
    ]

if __name__ == "__main__":
    start_game()