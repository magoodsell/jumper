import random
#from game.guess import Guess


class Word: 

    def __init__(self):
        """Get a word from the list to guess.

        Args:
            self (Word): An instance of Word.
        """
        _words = ['cat', 'rexburg', 'house', 'chapel', 'football', 'super']
        #open('jumper\words.txt') 
        self.show_letters = None
        self._words = random.choice(_words)
        self.new_word = []
        #self._test = Guess()


    def set_word(self):

        return self._words

    def get_word(self):

        self.new_word    #self._test.check_guess()
        pass

    def display_word(self):

        self.new_word = self.new_word       #self._test.check_guess()
        return self.new_word


    def get_words(self):

        """Show the underscore lines with the lengh.

        Args:
            self (Word): An instance of Word.
        """
        
        self.show_letters = " _ "*len(self._words)
        return self.show_letters
    
