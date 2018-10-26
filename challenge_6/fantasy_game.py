import random


class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.health = 100
        self.attack = 20
        self.name = name
        self.gold = 0


class Monster:
    """Represents a monster in the game that can attack a player."""
    def __init__(self, health, attack):
        self. health = health
        self.attack = attack


class Game:
    def play_game(self):
        """Call this method to start the game."""
        player = Player(input("What is your name?"))
        while player.health > 0:
            input("Press t to start another turn")
            n = random.randint(0, 3)
            if n == 0:
                if self.monster_attack(player):
                    break
            elif n == 1:
                self.find_gold(player)
            else:
                print("Nothing happened!")

    def monster_attack(self, player):
        """Called when a monster attacks a player."""
        monster = Monster(random.randint(0, 20), random.randint(0, 20))
        print("{} you are being attacked by a monster!".format(player.name))
        health = player.health
        while True:
            monster.health -= player.attack
            player.health -= monster.attack
            if monster.health < 0 or player.health < 0:
                break
        if player.health <= 0:
            print("You died!")
            print("Game over! You collected {} pieces of gold".format(player.gold))
            return True
        else:
            print("You lost {} health. Your health is now {}.".format(health - player.health, player.health))

    def find_gold(self, player):
        """Called when a player finds gold."""
        gold_found = random.randint(0, 100)
        player.gold += gold_found
        print("{} you found {} gold. You have {} gold.".format(player.name, gold_found, player.gold))


game = Game()
game.play_game()