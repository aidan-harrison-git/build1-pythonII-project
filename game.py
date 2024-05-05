class Game():
    def __init__(self, beg_ntg, beg_stg, player_name):
        self.guessed_letters = []
        self.guesses_count = 0
        self.beg_ntg = beg_ntg
        self.beg_stg = beg_stg
        self.player_name = player_name
        self.curr_guess = self.guess() 
        self.curr_str = ''
        
    def guess(self):
        if self.guesses_count == 0: 
            print(f'\n{self.beg_stg} is your string to guess\n') # prints the number of hashes corresponding to the length of the name, as established in names.py
        else:
            pass

        while True: # active until an acceptable guess it made
            letter = str(input('Guess a lowercase letter: ')).lower()
            if letter.isalpha() == True and len(letter) == 1: # tests for acceptable input
                break
            else:
                print('Invalid input. Please enter a single lowercase letter: ') # guides user to make an acceptable input

        while letter.lower() in self.guessed_letters:
                letter = input('Guess a new letter: ') # protects against guessing the same letter twice
        
        self.guessed_letters.append(letter.lower()) # once a proper guess is made, added to list of guessed letters
        if self.guesses_count == 0:
            self.guesses_count += 1 

        return letter 

    def replace(self):
        if self.guesses_count == 1: # turns the name and string into lists for in place edits
            list_ntg = list(self.beg_ntg)
            list_stg = list(self.beg_stg)
        else:
            list_ntg = list(self.updated_name)
            list_stg = list(self.updated_str)

        if self.guesses_count > 1: # compares a new guess letter to its presence / lack thereof in professor's name
            curr_guess = self.guess() # a new guess is created after guess 1 because the cycle() function in line 77 repeats the replace() function only
            for name_letter in list_ntg:
                if  curr_guess == name_letter:
                    x_index = list_ntg.index(name_letter)
                    list_stg[x_index] = name_letter.upper()
                    if list_ntg.count(name_letter) > 1: # allows the program to check for multiple occurrences of the same letter instead of just the first
                        list_ntg[x_index] = '#'
        else: # does the same as above but when the user has just taken their first guess
            for name_letter in list_ntg: 
                if self.curr_guess == name_letter:
                    x_index = list_ntg.index(name_letter)
                    list_stg[x_index] = name_letter.upper()
                    if list_ntg.count(name_letter) > 1:
                        list_ntg[x_index] = '#'
        
        updated_str = ''.join(list_stg) 
        updated_name = ''.join(list_ntg)
        
        self.curr_str = updated_str # updates the variable in the constructor for use in next iteration of replace()

        self.updated_str = updated_str # updates the variable in the constructor for use in next iteration of replace()
        self.updated_name = updated_name # updates the variable in the constructor for use in next iteration of replace()

        if updated_str.lower() == self.beg_ntg.lower():
            print(f'{updated_str} is your updated string\n')
            print(f'{self.player_name}, you won the game! Thanks for playing!\n') # win message if string matches professor's name
        elif self.guesses_count == 12:
            print(f'{updated_str} is your updated string\n')
            print(f'{self.player_name}, you failed to guess {self.beg_ntg.upper()}. Thanks for playing!\n') # loss message if user exhausts 12 guesses without matching string to name
        else:
            print(f'\n{updated_str} is your updated string\n')
            print(f'You have guessed: \n{self.guessed_letters} \nYour guesses total {len(self.guessed_letters)} of 12') # message after each non-win/loss guess

        return 

    def cycle(self):
        while self.guesses_count < 13 and self.curr_str.lower() != self.beg_ntg.lower(): # loop to accept up to 12 acceptable guesses
            if self.guesses_count == 0: # guesses count is incremented by 1 in the guess() function on the first guess
                pass
            else:
                self.replace()
                self.guesses_count += 1
        return 