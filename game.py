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
            print(f'\n{self.beg_stg} is your string to guess\n')
        else:
            pass

        while True:
            letter = str(input('Guess a lowercase letter: '))
            if letter.isalpha() == True and len(letter) == 1:
                break
            else:
                print('Invalid input. Please enter a single lowercase letter: ')

        while letter in self.guessed_letters:
                letter = input('Guess a new letter: ')
        
        self.guessed_letters.append(letter)
        if self.guesses_count == 0:
            self.guesses_count += 1

        return letter

    def replace(self):
        if self.guesses_count == 1:
            list_ntg = list(self.beg_ntg)
            list_stg = list(self.beg_stg)
        else:
            list_ntg = list(self.updated_name)
            list_stg = list(self.updated_str)

        if self.guesses_count > 1:
            curr_guess = self.guess()
            for name_letter in list_ntg:
                if  curr_guess == name_letter:
                    x_index = list_ntg.index(name_letter)
                    list_stg[x_index] = name_letter.upper()
                    if list_ntg.count(name_letter) > 1:
                        list_ntg[x_index] = '#'
        else:
            for name_letter in list_ntg:
                if self.curr_guess == name_letter:
                    x_index = list_ntg.index(name_letter)
                    list_stg[x_index] = name_letter.upper()
                    if list_ntg.count(name_letter) > 1:
                        list_ntg[x_index] = '#'
        
        updated_str = ''.join(list_stg)
        updated_name = ''.join(list_ntg)
        
        self.curr_str = updated_str

        self.updated_str = updated_str
        self.updated_name = updated_name

        if updated_str.lower() == self.beg_ntg.lower():
            print(f'{updated_str} is your updated string\n')
            print(f'{self.player_name}, you won the game! Thanks for playing!\n')
        elif self.guesses_count == 12:
            print(f'{updated_str} is your updated string\n')
            print(f'{self.player_name}, you failed to guess the name. Thanks for playing!\n')
        else:
            print(f'{updated_str} is your updated string\n')
            print(f'You have guessed: \n{self.guessed_letters} \nYour guesses total {len(self.guessed_letters)} of 12')

        return 

    def cycle(self):
        while self.guesses_count < 13 and self.curr_str.lower() != self.beg_ntg.lower():
            if self.guesses_count == 0:
                pass
            else:
                self.replace()
                self.guesses_count += 1
        return 