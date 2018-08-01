import random


class Rps:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.quit = 'q'
        self.message = "You picked {} and the computer picked {}. You {}!"

    def get_input(self):
        uinput = input("Choose {} {} or {}. Type {} to quit: \n".format(self.choices[0], self.choices[1], self.choices[2], self.quit))
        if uinput == self.quit:
            return self.quit
        if uinput not in self.choices:
            print("invalid option")
            return
        return uinput

    def player_won(self, player_choice, comp_choice):
        win_dict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        if win_dict[player_choice] == comp_choice:
            return 0
        if win_dict[comp_choice] == player_choice:
            return 1
        return 2

    def start_game(self):
        while True:
            player_choice = self.get_input()
            if player_choice == self.quit:
                break
            if not player_choice:
                continue
            comp_choice = self.choices[random.randint(0, 2)]
            result = self.player_won(player_choice, comp_choice)
            print(self.message.format(player_choice, comp_choice, {0: "won", 1: "lost", 2: "tied"}[result]))


game = Rps()
game.start_game()
