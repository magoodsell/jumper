import random


class Word: 

    def __init__(self):
        """Get a word from the list to guess.

        Args:
            self (Word): An instance of Word.
        """
        _words = open('words.txt')
        show_letters = None
        self._words = random.choice(_words)


       

    def get_words(self):

        """Get a word from the list to guess.

        Args:
            self (Word): An instance of Word.
        """
        show_letters = None
        self.show_letters = list("_"*len(self._words))
        return self._words
    
