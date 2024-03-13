import names
import player
import random
import game

# class Round():
#     def __init__(self):
#         self.curr_round_num = 0
#         self.curr_round_p = self.create_player()
#         self.curr_round_name = self.create_name()
#         self.curr_round_game = self.create_game()
#         self.curr_guess = self.curr_round_game.curr_guess
#         self.response = self.curr_round_game.updated_str
#         self.guess = self.curr_round_game.guess()
#         self.replace = self.curr_round_game.replace()

#     def create_player(self):
#         player_name = input('What is your name? ')
#         p = player.Player(player_name)
#         return p

#     def create_name(self):
#         name = names.Names(self.curr_round_p)
#         return name

#     def create_game(self):
#         curr_ntg = self.curr_round_name.curr_ntg
#         curr_stg = self.curr_round_name.curr_stg

#         g = game.Game(curr_ntg, curr_stg)
#         return g

#     def update_string(self):
#         updated_str = self.curr_round_game.updated_str
#         curr_guess = self.curr_round_game.curr_guess
#         return f'{curr_guess} is your guess and {updated_str} is your updated string to guess.'

#     def play_game(self):
#         for num in range(0, 13):
#             print(self.response)

class Round():
    def __init__(self, player_name):
        # super().__init__()
        self.curr_round_num = 0
        self.player_name = player_name
        self.player = player.Player(player_name)
        self.name = names.Names(self.player)
        self.game = game.Game(self.name.curr_ntg, self.name.curr_stg)
        # self.resp = self.response()
        self.runtime = self.game.cycle()

    # def response(self):
    #     curr_guess = self.game.curr_guess
    #     updated_str = self.game.updated_str
    #     return f'{curr_guess} is your guess and {updated_str} is your updated string to guess.'

    # def play_game(self):
    #     for num in range(0, 13):
    #         self.response()