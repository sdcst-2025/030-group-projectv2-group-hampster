import random
import time

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.health = 100
        self.attack_power = 10 + (self.level * 2)

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack_power = 10 + (self.level * 2)

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.experience -= 100
            self.level_up()

class Enemy:
    def __init__(self, level):
        self.level = level
        self.health = 50 + (level * 10)
        self.attack_power = 5 + (level * 2)

    def deal_damage(self):
        return random.randint(1, self.attack_power)

class Game:
    def __init__(self):
        self.character = None
        self.enemies = []
        self.dungeon = True

    def start_menu(self):
        print("Welcome to the RPG Game!")
        name = input("Enter your character's name: ")
        char_class = input("Choose your class (Warrior, Mage, Archer): ")
        self.character = Character(name, char_class)
        print(f"{self.character.name} the {self.character.char_class} has entered the game!")

    def create_enemies(self):
        for i in range(5):
            self.enemies.append(Enemy(random.randint(1, self.character.level + 2)))

    def dungeon_explore(self):
        self.create_enemies()
        while self.dungeon:
            print("\nYou are in a dungeon. You can explore or check your status.")
            action = input("Choose an action (explore/status/exit): ").lower()
            if action == "explore":
                self.fight_enemy()
            elif action == "status":
                self.show_status()
            elif action == "exit":
                self.dungeon = False
            else:
                print("Invalid action.")

    def fight_enemy(self):
        enemy = random.choice(self.enemies)
        print(f"A wild enemy of level {enemy.level} appears!")
        while enemy.health > 0 and self.character.health > 0:
            print(f"{self.character.name} attacks the enemy!")
            enemy.health -= self.character.attack_power
            print(f"Enemy health: {enemy.health}")
            if enemy.health > 0:
                damage = enemy.deal_damage()
                self.character.health -= damage
                print(f"Enemy attacks! {self.character.name} takes {damage} damage. Health: {self.character.health}")
        if self.character.health <= 0:
            print("You have been defeated!")
            self.dungeon = False
        else:
            print("You defeated the enemy!")
            loot = random.randint(10, 30)
            self.character.gain_experience(loot)
            print(f"You gained {loot} experience!")

    def show_status(self):
        print(f"Name: {self.character.name}, Class: {self.character.char_class}, Level: {self.character.level}, Health: {self.character.health}, Experience: {self.character.experience}")

if __name__ == "__main__":
    game = Game()
    game.start_menu()
    game.dungeon_explore()