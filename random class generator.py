import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define all possible classes
CLASSES = [
    "Mage", "Warrior", "Rogue", "Ninja", "Paladin", "Priest",
    "Necromancer", "Archer", "Bard", "Samurai", "Assassin",
    "Trickster", "Kensei", "Sorcerer"
]

# Item rarities and their damage multipliers
RARITY_DAMAGE = {
    "Common": 5,
    "Uncommon": 10,
    "Rare": 20,
    "Legendary": 40
}

# Item pool categorized by class
ITEMS = {
    "Mage": ["Magic Staff", "Spellbook"],
    "Warrior": ["Iron Sword", "Battle Axe"],
    "Rogue": ["Dagger", "Poison Vial"],
    "Ninja": ["Kunai", "Shuriken"],
    "Paladin": ["Holy Sword", "Blessed Shield"],
    "Priest": ["Healing Staff", "Sacred Scroll"],
    "Necromancer": ["Bone Wand", "Dark Grimoire"],
    "Archer": ["Longbow", "Quiver of Arrows"],
    "Bard": ["Lute", "Flute of Enchantment"],
    "Samurai": ["Katana", "War Fan"],
    "Assassin": ["Hidden Blade", "Poison Dart"],
    "Trickster": ["Jester's Dagger", "Trick Coin"],
    "Kensei": ["Master Katana", "Spirit Charm"],
    "Sorcerer": ["Ancient Spellbook", "Enchanted Orb"],
}

# Abilities categorized by class
ABILITIES = {
    "Mage": "Fireball - Deals massive magic damage.",
    "Warrior": "Berserk - Increases attack damage temporarily.",
    "Rogue": "Backstab - Deals critical damage from behind.",
    "Ninja": "Shadow Step - Evade an attack completely.",
    "Paladin": "Divine Shield - Temporarily immune to damage.",
    "Priest": "Healing Light - Restores health.",
    "Necromancer": "Summon Undead - Calls a minion for aid.",
    "Archer": "Rain of Arrows - Attacks all enemies at once.",
    "Bard": "Inspiring Tune - Boosts team morale and stats.",
    "Samurai": "Blade Dance - A flurry of fast strikes.",
    "Assassin": "Silent Kill - Instant kill weak enemies.",
    "Trickster": "Illusion - Confuse the enemy for a turn.",
    "Kensei": "Precision Strike - Increased accuracy and damage.",
    "Sorcerer": "Arcane Blast - Area damage spell."
}

# Enemy types
ENEMIES = [
    {"name": "Goblin", "hp": 30, "damage": 5},
    {"name": "Skeleton", "hp": 40, "damage": 8},
    {"name": "Orc", "hp": 50, "damage": 12},
    {"name": "Dark Mage", "hp": 60, "damage": 15},
    {"name": "Demon", "hp": 70, "damage": 18},
    {"name": "Dragon", "hp": 100, "damage": 25}
]

# Function to determine an item's rarity
def get_item_rarity():
    roll = random.randint(1, 100)
    if roll <= 5:
        return "Legendary"
    elif roll <= 20:
        return "Rare"
    elif roll <= 50:
        return "Uncommon"
    else:
        return "Common"

# Function to generate loot with damage values
def generate_loot(character_class):
    available_items = ITEMS.get(character_class, ["Mystery Item"])
    item_name = random.choice(available_items)
    rarity = get_item_rarity()
    damage = RARITY_DAMAGE[rarity]
    return {"name": item_name, "rarity": rarity, "damage": damage}

# Function for interactive menu between levels
def level_interaction(player_name, stats, inventory):
    while True:
        clear_screen()
        print("\n📜 LEVEL MENU 📜")
        print("1. View Character Stats")
        print("2. View Inventory")
        print("3. Continue Journey")
        choice = input("Choose an option: ")
        if choice == "1":
            clear_screen()
            print(f"\n🎲 {player_name} Stats 🎲")
            for stat, value in stats.items():
                print(f"{stat}: {value}")
        elif choice == "2":
            clear_screen()
            print("\n🧳 Inventory:")
            for item in inventory:
                print(f" - {item['rarity']} {item['name']} ({item['damage']} DMG)")
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")
        input("\nPress Enter to continue...")

# Function for combat
def combat(player_name, weapon, level):
    enemy = random.choice(ENEMIES)
    enemy_hp = enemy["hp"] + (level * 5)
    player_hp = 100
    while enemy_hp > 0 and player_hp > 0:
        clear_screen()
        print(f"\n Level {level}: A {enemy['name']} appears! ({enemy_hp} HP, {enemy['damage']} DMG)")
        print(f"\n{player_name}: {player_hp} HP | {enemy['name']}: {enemy_hp} HP")
        action = input("Attack (A) or Flee (F)? ").strip().lower()
        if action == 'a':
            enemy_hp -= weapon["damage"]
            player_hp -= enemy["damage"] if enemy_hp > 0 else 0
        elif action == 'f':
            print("🏃 You fled safely!")
            return False
        else:
            print("Invalid input!")
    return player_hp > 0

# Character creation
clear_screen()
name = input("Enter your character's name: ")
age = int(input("Enter your character's age: "))
character_class = random.choice(CLASSES)
weapon = generate_loot(character_class)
ability = ABILITIES[character_class]
inventory = [weapon]
stats = {"Level": 1, "HP": 100, "Mana": 50}

for level in range(1, 11):
    level_interaction(name, stats, inventory)
    if not combat(name, weapon, level):
        print("Game Over!")
        break
else:
    print("🏆 Congratulations! You completed the journey!")
