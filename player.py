class Player():
    def __init__(self, player_name, department):
        self.player_name = player_name
        self.guessed_letters = []
        self.department = department
    def guess_letter(self, letter):
        self.guessed_letters.append(letter)
