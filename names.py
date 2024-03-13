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
    
        self.curr_ntg = self.generate_name(player)
        self.curr_stg = self.generate_string()


    def generate_name(self, player):
        name_index = random.randint(0, len(self.directory[player.department])-1)
        curr_ntg = self.directory[player.department][name_index].lower()

        return curr_ntg

    def generate_string(self):
        
        for num in range(len(self.curr_ntg)):
            self.string_to_guess_list.append('#')

        curr_stg = ''.join(self.string_to_guess_list)

        return curr_stg

