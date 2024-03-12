import random

import components
import player
import game

class Names():
    directory = {'art_sci':['Dewise', 'Collins'], 
                'bus':['Vega', 'Greenlee'], 
                'bib':['Soko', 'Gardner'], 
                'edu':['Bean', 'Smith']
    }
    def __init__(self, player):    
        self.string_to_guess_list = []
        # self.string_to_guess = '-'.join(self.string_to_guess_list)
        # self.name_selected = ''
        self.curr_ntg = self.generate_name(player)
        self.curr_stg = self.generate_string()


    def generate_name(self, player):
        name_index = random.randint(0, len(self.directory[player.department])-1)
        curr_ntg = self.directory[player.department][name_index]
        
        # for character in self.name_selected:
        #     self.string_to_guess_list.append('X')
        
        # print('Your name to guess: ')
        # self.string_to_guess = '-'.join(self.string_to_guess_list)

        return curr_ntg

    def generate_string(self):
        
        for num in range(len(self.curr_ntg)):
            self.string_to_guess_list.append('X')

        curr_stg = '-'.join(self.string_to_guess_list)

        return curr_stg

