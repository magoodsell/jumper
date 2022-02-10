import guess
import word
class terminal:

    def __init__(self):
        self.guess= guess
        self._failedGuesses = guess.set_wrong_guesses()
        self._Word = word.get_word()
        
    def newWord(self):
        self.word
   # get word form word
   # make of get the wrong choice
    def results(self):

        if guess != self.guess.getletter():
            if self._failedGuesses == 1:
                print(" --- ")
                print("/   \ ")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif self._failedGuesses == 2:  
                print("")
                print("/   \ ")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif self._failedGuesses == 3:
                print("")
                print("")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif self._failedGuesses == 4:
                print("")
                print("")
                print("")
                print("")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif self._failedGuesses == 5:
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
