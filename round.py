import names
import player
import game
# instantiates player object, names object, game object using their required inputs
class Round():
    def __init__(self, player_name):
        self.curr_round_num = 0
        self.player_name = player_name
        self.player = player.Player(player_name)
        self.name = names.Names(self.player)
        self.game = game.Game(self.name.curr_ntg, self.name.curr_stg, self.player_name)      