

class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.department = self.department_select()
    
    def print_dept_options(self):
        dept_strings = ['a) Arts & Sciences', 'b) Biblical Studies', 'c) Business', 'd) Education & Social Sciences']
        print("\n Select the letter corresponding to your major's department: \n")
        for dept in dept_strings:
            print(f'{dept} \n')
        return 'Selection: '

    def department_select(self):
        department_selection = input(self.print_dept_options())
        if department_selection == 'a' or department_selection == 'a)' or department_selection == 'A':
            return 'art_sci'
        elif department_selection == 'b' or department_selection == 'b)' or department_selection == 'B':
            return 'bib'
        elif department_selection == 'c' or department_selection == 'c)' or department_selection == 'C':
            return 'bus'
        elif department_selection == 'd' or department_selection == 'd)' or department_selection == 'D':
            return 'edu'
        else:
            print('Please try again...')
        return self.print_dept_options()

    
