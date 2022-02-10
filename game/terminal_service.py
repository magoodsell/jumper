#from game.guess import Guess
#from game.word import Word


class terminal:

    def __init__(self):
        self._guess = None
        self._failedGuesses = 0
        self._Word = None
        
    def newWord(self):
        self._Word
        pass

    def display_word(self, word):
        
        print(f'{word}\n')

            # print the updated each time

    def user_prompt(self):
        letter = input('select a letter from [a-z]: ')
        print()
        return letter


   # get word form word
   # make of get the wrong choice
    def results(self):

        # if guess != self.guess.getletter():
        if self._failedGuesses == 0:
            print(" ----- ")
            print("/     \ ")
            print("-------")
            print("\     /")
            print(" \   / ")
            print("   O  " )
            print("/  |  \ ")
            print("  / \ " )
            print("^^^^^^^^")
        elif self._failedGuesses == 1:  
            print("")
            print("/     \ ")
            print("-------")
            print("\     /")
            print(" \   / ")
            print("   O  ")
            print("/  |  \ ")
            print("  / \ ")
            print("^^^^^^^^")
        elif self._failedGuesses == 2:
            print("")
            print("")
            print("-------")
            print("\     /")
            print(" \   / ")
            print("   O  ")
            print("/  |  \ ")
            print("  / \ ")
            print("^^^^^^^^")
        elif self._failedGuesses == 3:
            print("")
            print("")
            print("")
            print("")
            print(" \   / ")
            print("   O  ")
            print("/  |  \ ")
            print("  / \ ")
            print("^^^^^^^^")
        elif self._failedGuesses == 4:
            print("")
            print("")
            print("")
            print("")
            print("")
            print ("  X  " )
            print("/  |  \ ")
            print("  / \ " )
            print("^^^^^^^^")


gameOver = True
