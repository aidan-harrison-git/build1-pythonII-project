import player
import game
import names
import round

get_name = input('What is your name? ')

round1 = round.Round(get_name)
round1.game.cycle()




