import guess
import word
class terminal:

    def __init__(_self):
        _self.guess= guess

        failedGuesses = 0
   # get word form word
   # make of get the wrong choice
    def results(self):
        failedGuesses = 0
        if guess != self.guess.getletter():
            if failedGuesses == 1:
                print(" --- ")
                print("/   \ ")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif failedGuesses == 2:  
                print("")
                print("/   \ ")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif failedGuesses == 3:
                
                print("")
                print("")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif failedGuesses == 4:
                print("")
                print("")
                print("")
                print("")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("^^^^^^^^")
            elif failedGuesses == 5:
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
