class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.department = self.department_select()
    
    def print_dept_options(self):
        dept_strings = ['a) Behavioral Sciences', 'b) Education', 'c) Math, Engineering, & CompSci', 'd) Business', 'e) Nursing', 'f) Bio, Physical, & Health Sciences', 'g) Arts & Humanities', 'h) Comms & Creative Arts', 'i) Biblical Studies']
        print("\n Select the letter corresponding to your major's department: \n")
        for dept in dept_strings:
            print(f'{dept} \n')
        return 'Selection: '

    def department_select(self):
        department_selection = input(self.print_dept_options())
        if department_selection in ['a', 'a ', 'a)', 'a) ', 'A', 'A ', 'A)', 'A) ']:
            return 'BS'
        elif department_selection in ['b', 'b ', 'b)', 'b) ', 'B', 'B ', 'B)', 'B) ']:
            return 'EDU'
        elif department_selection in ['c', 'c ', 'c)', 'c) ', 'C', 'C ', 'C)', 'C) ']:
            return 'MECS'
        elif department_selection in ['d', 'd ', 'd)', 'd) ', 'D', 'D ', 'D)', 'D) ']:
            return 'BUS'
        elif department_selection in ['e', 'e ', 'e)', 'e) ', 'E', 'E ', 'E)', 'E) ']:
            return 'NSG'
        elif department_selection in ['f', 'f ', 'f)', 'f) ', 'F', 'F ', 'F)', 'F) ']:
            return 'BPHS'
        elif department_selection in ['g', 'g ', 'g)', 'g) ', 'G', 'G ', 'G)', 'G) ']:
            return 'A&H'
        elif department_selection in ['h', 'h ', 'h)', 'h) ', 'H', 'H ', 'H)', 'H) ']:
            return 'CCA'
        elif department_selection in ['i', 'i ', 'i)', 'i) ', 'I', 'I ', 'I)', 'I) ']:
            return 'BIB'
        else:
            print('Please try again...')
        return self.print_dept_options()