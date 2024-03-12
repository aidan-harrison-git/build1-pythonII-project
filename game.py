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
        # self.string = self.generate_name(self)
        self.curr_guess = self.guess()
        self.updated_str = self.replace()
        
        

    def guess(self):
        letter = input('Guess a letter: ')

        if letter in self.guessed_letters:
                letter = input('Guess a new letter: ')
        else:
            self.guessed_letters.append(letter)
            self.guesses_count += 1

        return letter

    def replace(self):

        print(self.beg_stg)

        list_ntg = list(self.beg_ntg)
        list_stg = list(self.beg_stg)
        
        print(list_ntg)
        print(list_stg)

        for name_letter in list_ntg:
            if name_letter == self.curr_guess:
                x_index = list_ntg.index(name_letter)
                list_stg[x_index] = name_letter
        
        updated_str = '-'.join(list_stg)

        return updated_str
























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



    
    