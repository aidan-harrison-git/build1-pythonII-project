import round

play_again = 'yes' # yes by default; simplifies input from line 13 by understanding anything other than 'NO', 'No', or 'no' to be a positive indicator

# giving game rules / instructions to the user
print('\nThis game will challenge you to guess the name of a professor in your department.')
print('\nYou will have 12 opportunities to guess a letter. Each guess will be applied to the hidden name.')
print('\nTo win, reveal the name before you exhaust your guesses!')

while play_again != 'no':
    get_name = input('\nDesignate a username: ') # creates username for purpose of addressing the user in messages 
    curr_round = round.Round(get_name) # instantiates a round which in turn instantiates objects of player, names, and game
    curr_round.game.cycle()  # runs the game file's cycle function which loops until 12 guesses are exhausted or win condition is met
    play_again = input('Would you like to play again? yes/no: ').lower()