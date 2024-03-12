import player
import game
import names
import components

# def print_dept_options():
#     dept_strings = ['a) Arts & Sciences', 'b) Biblical Studies', 'c) Business', 'd) Education & Social Sciences']
#     print("\n Select the letter corresponding to your major's department: \n")
#     for dept in dept_strings:
#         print(f'{dept} \n')
#     return 'Selection: '

# def department():
#     department_selection = input(print_dept_options())
#     if department_selection == 'a' or department_selection == 'a)' or department_selection == 'A':
#         return 'art_sci'
#     elif department_selection == 'b' or department_selection == 'b)' or department_selection == 'B':
#         return 'bib'
#     elif department_selection == 'c' or department_selection == 'c)' or department_selection == 'C':
#         return 'bus'
#     elif department_selection == 'd' or department_selection == 'd)' or department_selection == 'D':
#         return 'edu'
#     else:
# #         print('Please try again...')
#     department()
    

aidan = player.Player('Aidan')

round1_names = names.Names(aidan)

# round1_names.curr_ntg = round1_names.generate_name(aidan)
# round1_names.curr_stg = round1_names.generate_string()
# print(f'{round1_names.curr_stg} is your string to guess')

curr_ntg = round1_names.curr_ntg
curr_stg = round1_names.curr_stg
print(curr_ntg)
print(curr_stg)

round1_game = game.Game(curr_ntg, curr_stg)

# r1_name = round1_names.generate_name(aidan)
# r1_str = round1_names.generate_string()

curr_guess = round1_game.curr_guess
print(round1_game.updated_str)
updated_str = round1_game.updated_str

print(f'{curr_guess} is your guess.')
print(f'{updated_str} is your updated string to guess.')



