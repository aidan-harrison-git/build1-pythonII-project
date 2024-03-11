import random
import player

class Names():
    directory = {'art_sci_names':[], 
                'bus_names':[], 
                'bib_names':[], 
                'edu_names':[]
    }
    def __init__(self):    
        self.string_to_guess = 'x'

    def generate_name(self):
        name_index = random.randint(0, len(self.directory[player.department]))
        name_selected = self.directory[player.department][name_index]

