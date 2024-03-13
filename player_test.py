import round

play_again = 'yes'

while play_again != 'no':
    get_name = input('\nDesignate a username: ')
    round1 = round.Round(get_name)
    round1.game.cycle() 
    play_again = input('Would you like to play again? yes/no: ').lower()

