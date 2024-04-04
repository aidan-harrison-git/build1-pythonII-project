class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.department = self.department_select()
    
    def print_dept_options(self):
        dept_strings = ['a) Arts & Sciences', 'b) Biblical Studies', 'c) Business', 'd) Education & Behavioral Sciences']
        print("\n Select the letter corresponding to your major's department: \n")
        for dept in dept_strings:
            print(f'{dept} \n')
        return 'Selection: '

    def department_select(self):
        department_selection = input(self.print_dept_options())
        if department_selection in ['a', 'a ', 'a)', 'a) ', 'A', 'A ', 'A)', 'A) ']:
            return 'art_sci'
        elif department_selection in ['b', 'b ', 'b)', 'b) ', 'B', 'B ', 'B)', 'B) ']:
            return 'bib'
        elif department_selection in ['c', 'c ', 'c)', 'c) ', 'C', 'C ', 'C)', 'C) ']:
            return 'bus'
        elif department_selection in ['d', 'd ', 'd)', 'd) ', 'D', 'D ', 'D)', 'D) ']:
            return 'edu'
        else:
            print('Please try again...')
        return self.print_dept_options()

    
