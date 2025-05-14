# William Foster
# 4-29-25
# P5HW
# This is a game where you can pick your weapon

import random

def create_character():
    name = input("Enter your character's name: ")
    print("\nChoose your weapon:")
    print("1. Sword")
    print("2. Magic Staff")
    weapon_choice = input("Enter 1 or 2: ")

    if weapon_choice == "1":
        weapon = "Sword"
        base_damage = 15
    elif weapon_choice == "2":
        weapon = "Magic Staff"
        base_damage = 0
    else:
        print("Invalid choice. Defaulting to Sword.")
        weapon = "Sword"
        base_damage = 15

    character = {
        "name": name,
        "health": 100,
        "weapon": weapon,
        "base_damage": base_damage
    }

    return character

def display_character(character):
    print("\nCharacter:")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

def attack(player, enemy):
    if player["weapon"] == "Sword":
        damage = player["base_damage"]
    else:
        damage = random.choice([5, 10, 20])

    print(f"\n{player['name']} attacks the {enemy['name']} with a {player['weapon']}!")
    enemy["health"] -= damage
    if enemy["health"] < 0:
        enemy["health"] = 0
    print(f"The {enemy['name']} has {enemy['health']} HP left.")

def create_enemy(name, health):
    return {
        "name": name,
        "health": health
    }

def main():
    print("Welcome to the Game!")

    player = create_character()
    display_character(player)

    goblin = create_enemy("Goblin", 30)
    print("\nA Goblin appears!")

    while goblin["health"] > 0:
        input("Press Enter to attack...")
        attack(player, goblin)

    print("\n✅ Goblin defeated.")

    golem = create_enemy("Stone Golem", 60)
    print("\n💀 Stone Golem appears!")

    while golem["health"] > 0:
        input("Press Enter to attack...")
        attack(player, golem)

    print("\n✅ Stone Golem defeated. You win!")

main()
