import round

play_again = 'yes'

print('This game will challenge you to guess the name of a professor in your department.')
print('\nYou will have 12 opportunities to guess a letter. Each guess will be applied to the hidden name.')
print('\nTo win, reveal the name before you exhaust your guesses!')

while play_again != 'no':
    get_name = input('\nDesignate a username: ')
    curr_round = round.Round(get_name)
    curr_round.game.cycle() 
    play_again = input('Would you like to play again? yes/no: ').lower()

