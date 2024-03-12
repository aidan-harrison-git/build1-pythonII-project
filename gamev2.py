import names
import components
import player
import random


class Game():
    def __init__(self):
        self.guessed_letters = []
        self.guesses_count = 0
        self.string = self.generate_name(self)
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

    def replace(self, names_instance):

        list_string_to_guess = names_instance.string_to_guess.split('-')
        list_name_selected = names_instance.name_selected.split()

        for name_letter in list_name_selected:
            if name_letter == self.curr_guess:
                x_index = list_name_selected.index(name_letter)
                list_string_to_guess[x_index] = name_letter
        
        updated_str = ''.join(list_string_to_guess)

        return updated_str
    

    