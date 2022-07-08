#? What I want to do: 
# Call a function/class to start the game.
# Have my word randomly chosen from hangmanaddon.py
# Try to guess the letters, I have 7 tries.

# LOGIC
# The code should know if there are multiple identical letters and sort the issue
# Print the hangman picture corresponding to the amount of incorrect words
# Display what words are correct and blank characters (=? py_th_n)
# Difficulty settings 0 - None, 1 - Words of max 10 letters, 2 - Words of max 14 letters


import hangmanaddon
import random

from typing import Optional

class Hangman():
    def __init__(self, difficulty : Optional[int] = None):
        self.difficulty = difficulty or 0

        self.word = None
    
        self.all = []
        self.possiblycorrect = []
        self.correct = []

        self.choose_word()
        self.game()

    def check(self, difficulty, word):
        match difficulty:
            case 0:
                return True
            case 1:
                if len(word) > 10:
                    return False
                else:
                    return True
            case 2:
                if len(word) > 14:
                    return False
                else:
                    return True

    def split(self, word):
        return list(dict.fromkeys(list(word)))

    def choose_word(self):
        i = 0
        while i < 10:
            word = hangmanaddon.words[random.randint(0, 212)]
            if self.check(self.difficulty, word):
                self.word = word
                self.possiblycorrect = self.split(word)
                break
            else: 
                pass

    def return_correct(self):
        return_value = ""
        for x in self.word:
            if x in self.correct:
                return_value += x
            else:
                return_value += '_'
        return return_value

    def game(self):
        while len(self.correct) < len(self.possiblycorrect):
            try:
                print(hangmanaddon.ASCII[len(self.all)], f'Incorrect letters so far: {",".join(self.all)}', f'Correct letters so far: {self.return_correct()}', sep='\n')
                inp = input('> ')[0]
                if inp in self.possiblycorrect:
                    if inp in self.correct:
                        print('You already chose that')
                    else:
                        print('Correct')
                        self.correct.append(inp)
                else:
                    print('Incorrect')
                    self.all.append(inp)
            except:
                print(f'You have lost, the word was: {self.word}')
                break
        print('Congratulations, you won!')

Hangman(1)
