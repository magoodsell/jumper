import guess
import word
class terminal:

    def __init__(self):
        self.guess= guess

   
   
    def results(self):
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
                print("“^^^^^^^^")
            elif failedGuesses == 2:  
                print("")
                print("/   \ ")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("“^^^^^^^^")
            elif failedGuesses == 3:
                
                print("")
                print("")
                print("------")
                print("\    /")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("“^^^^^^^^")
            elif failedGuesses == 4:
                print("")
                print("")
                print("")
                print("")
                print(" \  / ")
                print ("  O  " )
                print("/  |  \ ")
                print("  / \ " )
                print("“^^^^^^^^")
            elif failedGuesses == 5:
                print("")
                print("")
                print("")
                print("")
                print("")
                print ("  X  " )
                print("/  |  \ ")
                print("  / \ " )
                print("“^^^^^^^^")


	gameOver = True
