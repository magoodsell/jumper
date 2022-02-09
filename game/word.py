import random


class Word: 

    def __init__(self):
        """Get a word from the list to guess.

        Args:
            self (Word): An instance of Word.
        """
        _words = open('words.txt')
        self._words = random.choice(_words)

       

    def get_words(self):

        """Get a word from the list to guess.

        Args:
            self (Word): An instance of Word.
        """
        return self._words
    
