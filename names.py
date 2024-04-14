import random
import csv

class Names():
    with open('2023-2024 Faculty Information CSV.csv', 'r') as csvfile: # imports csv of professor names and their departments
        directory = {'BS':[], # dictionary where each key is a department and each value is a list of names in that department 
            'EDU':[],
            'MECS':[],
            'BUS':[],
            'NSG':[],
            'BPHS':[],
            'A&H':[],
            'CCA':[],
            'BIB':[]
        }
        
        professor_reader = csv.reader(csvfile, delimiter=',')

        index = 0

        for row in professor_reader: # professor last names parsed into their respective departments in the directory
            if index == 0:
                index += 1
                continue
            elif row[2] == 'BS':
                directory['BS'].append(row[0])
            elif row[2] == 'EDU':
                directory['EDU'].append(row[0])
            elif row[2] == 'MECS':
                directory['MECS'].append(row[0])
            elif row[2] == 'BUS':
                directory['BUS'].append(row[0])
            elif row[2] == 'NSG':
                directory['NSG'].append(row[0])
            elif row[2] == 'BPHS':
                directory['BPHS'].append(row[0])
            elif row[2] == 'A&H':
                directory['A&H'].append(row[0])
            elif row[2] == 'BIB':
                directory['BIB'].append(row[0])
            elif row[2] == 'CCA':
                directory['CCA'].append(row[0])
            else:
                pass

    def __init__(self, player): # requires a player object to act on for generating a name from their department 
        self.string_to_guess_list = [] # holds the number of hashes '#' matching the length of the name to guess
    
        self.curr_ntg = self.generate_name(player) # holds the return of the randomly generated professor's name
        self.curr_stg = self.generate_string() # holds the return of hashes matching the length of the  name


    def generate_name(self, player): # using the player object, randomly generates a last name of a professor in the player's department
        name_index = random.randint(0, len(self.directory[player.department])-1)
        curr_ntg = self.directory[player.department][name_index].lower()

        return curr_ntg

    def generate_string(self): # appends the number of hashes corresponding to the generated name to a list
        
        for num in range(len(self.curr_ntg)):
            self.string_to_guess_list.append('#')

        curr_stg = ''.join(self.string_to_guess_list)

        return curr_stg