#HANGMAN GAME

import random

class HangmanGame:
    def __init__(self):
        self.words = [
             'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
             'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
             'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
             'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
             'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
        ]

        self.stages = 0
        self.attempt = 6
        
    def player_guess (self):
        while True:
            try:
                option = input("Guess a leter : ").lower()
                if not isinstance(option,str) or len(option) != 1:
                    raise TypeError("Input must be a string or only one character")
                else:
                    break
            except TypeError as e:
                print("ERROR", e)
        
        return option
    
    def player_stages(self):
        stages = ["""
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """]
        
        return stages[self.stages]
     
    
    
    def play(self):
        pick_word = random.choice(self.words)
        
        fill_blank = ['_'] * len(pick_word)
        
        while self.stages < 6 and "_" in fill_blank:
             print("The word is : ", " ".join(fill_blank))
             word_guess = self.player_guess()
             
             cek = False
             
             for i,letter in enumerate(pick_word):
                 if letter == word_guess:
                    fill_blank[i] = letter
                    cek = True
            
             if cek == True:
                print("Correct!")
                print(self.player_stages())
             else:
                 self.attempt -= 1
                 self.stages += 1
                 print("Incorrect. You have {} attempts left ! ".format(self.attempt))
                 print(self.player_stages())
        
        if self.stages == 6 :
            print("Unfortunately the answer is : ",pick_word)
        else:
            print("Congratulations, you guess the right word : ",pick_word)
             
             
    def main(self):
        self.play()
    
    
    
game = HangmanGame()
game.main()

            
                    
                    
            
            
            
            
                
            
