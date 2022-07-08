# I am fu----- stupid
# I want a 3x3 matrix, where the >< is the point on the cube and __ empty space
#   [] __ []
#   [] __ []
#   [] __ []

# LOGIC
# I could make it WAAAY easier if I were just to do an ascii art and select that but no
# Get variations where the number 6 is str and is formated like this: '101101101' where 1 is [] and 0 is __

import random

class Dice:
    def __init__(self):
        self.variations = {
            1 : '000010000',
            2 : '100000001',
            3 : '100010001',
            4 : '101000101',
            5 : '101010101',
            6 : '101101101'
        }
        
        self.dot = '><'
        self.empty = '__'
        
        self.roll()


    def get_variation(self, roll):
        return self.variations[roll]

    def format(self, string):
        string = list(string)
        for index, a in enumerate(string):
            if int(a) == 0:
                string[index] = self.empty
            elif int(a) == 1:
                string[index] = self.dot
            
        for i in range(0, 9):
            string[i] = '|' + string[i] + '|'


        string[2] += '\n'
        string[5] += '\n'
        return ''.join(string)

    def roll(self):
        a = self.get_variation(random.randint(1, 6))
        print(self.format(a))
        
Dice()
