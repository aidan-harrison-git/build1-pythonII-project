import random
import csv

class Names():
    with open('2023-2024 Faculty Information CSV.csv', 'r') as csvfile:
        directory = {'BS':[],
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

        for row in professor_reader: 
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
            else:
                directory['CCA'].append(row[0])

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