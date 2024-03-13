import names
import components
import player
import random


class Game():
    def __init__(self, beg_ntg, beg_stg):
        self.guessed_letters = []
        self.guesses_count = 0
        self.beg_ntg = beg_ntg
        self.beg_stg = beg_stg
        self.curr_guess = self.guess()
        self.curr_str = ''
        
        
    def guess(self):
        if self.guesses_count == 0:
            print(f'\n{self.beg_stg} is your string to guess\n')
        else:
            pass

        letter = input('Guess a letter: ')

        if letter in self.guessed_letters:
                letter = input('Guess a new letter: ')
        else:
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
            print(f'{self.curr_guess} is your guess and {updated_str} is your updated string\n')
            print('You won the game! Thanks for playing!\n')
        elif self.guesses_count == 12:
            print(f'{self.curr_guess} is your guess and {updated_str} is your updated string\n')
            print('You failed to guess the name. Thanks for playing!\n')
        else:
            print(f'{self.curr_guess} is your guess and {updated_str} is your updated string\n')

        return 

    def response(self):
        curr_guess = self.curr_guess
        updated_str = self.updated_str
        return f'{curr_guess} is your guess and {updated_str} is your updated string to guess.'

    def cycle(self):
        while self.guesses_count < 13 and self.curr_str.lower() != self.beg_ntg.lower():
            if self.guesses_count == 0:
                pass
            else:
                self.replace()
                self.guesses_count += 1
        return 























# class Game():
#     def __init__(self):
#         self.guessed_letters = []
#         self.guesses_count = 0
#         self.string = self.generate_name(self)

#     def generate_name(self, player, names_instance):
#         name_index = random.randint(0, len(names_instance.directory[player.department])-1)
#         name_selection = names_instance.directory[player.department][name_index]
#         names_instance.name_selected = name_selection
        
#         for character in names_instance.name_selected:
#             names_instance.string_to_guess_list.append('X')
        
#         # print('Your name to guess: ')
#         names_instance.string_to_guess = '-'.join(names_instance.string_to_guess_list)

#         return names_instance.string_to_guess

#     def guess_and_replace(self, names_instance):
#         if self.guesses_count < 12:
#             letter = input('Guess a new letter: ')
#             if letter in self.guessed_letters:
#                 letter = input('Guess a new letter: ')
#             else:
#                 self.guessed_letters.append(letter)
#                 self.guesses_count += 1

#             # print('Thank you for your guess!')
        
#             list_string_to_guess = names_instance.string_to_guess.split('-')
#             list_name_selected = names_instance.name_selected.split()

#             for name_letter in list_name_selected:
#                 if name_letter == letter:
#                     x_index = list_name_selected.index(name_letter)
#                     list_string_to_guess[x_index] = name_letter
        
#             names_instance.string_to_guess_list = list_string_to_guess
#             names_instance.string_to_guess = ''.join(list_string_to_guess)

#             return f'Here is your updated name to guess: {names_instance.string_to_guess}'



    # def replace_letter(self, ntg_list, ntg):
    #     new_letter = self.guessed_letters[-1]
        
    #     list_string_to_guess = ntg_list
    #     list_name_selected = list(ntg.name_selected)

    #     for letter in list_name_selected:
    #         if new_letter == letter:
    #             x_index = list_name_selected.index(letter)
    #             list_string_to_guess[x_index] = letter
        
    #     names.string_to_guess_list = list_string_to_guess
    #     names.string_to_guess = ''.join(list_string_to_guess)

    #     return f'Here is your updated name to guess: {names.string_to_guess}'



    
    