


class Game():
    def __init__(self):
        self.guessed_letters = []
        self.guesses_count = 0

    def guess_letter(self):
        if self.guesses_count < 12:
            letter = input('Guess a new letter: ')
            if letter in self.guessed_letters == True:
                letter = input('Guess a new letter: ')
            self.guessed_letters.append(letter)
            self.guesses_count += 1
    
    