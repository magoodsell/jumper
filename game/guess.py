#from game.word import Word
#from game.terminal_service import terminal

#import terminal_service as terminal


class Guess:
    """ A guess from the player.
    The responsibility of the guess is to:
        - take the user guess and update the word displayed to the player. 
        - Keep track of wrong guesses made
        - Inform the player of duplicate guess 

    Attributes:
        self._guess (string): an empty string
        self._word (Word): the random word
        self._all_guesses (list): a list of all guess made.
        self._wrong_guesses (int): count of all wrong guesses made.

    """


    def __init__(self):
        """Constructs a new guess.
        
        Args:
            self (Guess): an instance of Guess.
        """

        self._let_guess = None
        self._word = None        #Word.set_word() 
        self._all_guesses = []
        self._wrong_guesses = 0
        self._tick = 0


         

    def get_guess(self):
        """
        Purpose is to get the word the person has guessed and append to _all_guesses
        """
        return self._all_guesses.append(self._let_guess)


    def get_wrong_guesses(self):

        return self._wrong_guesses

    def set_wrong_guesses(self):

        self._wrong_guesses += self._tick
        return self._wrong_guesses

    def get_word(self, word):

        self._word = word

    def check_duplicate(self, guess):
        """purpose is to make sure the player is not guessing the same letter
        If so will need to send a message to the terminal to prompt them to guess again. 
        """
        for i in len(self._all_guesses):
            if guess == i:
                print(f"'{guess}' has been chosen.\nPlease guess again.\n")
        pass
        

    def check_guess(self):
        """
        Checks the guess to make sure it matches a letter and returns an updated word.
        """
        new_word = []               
        self._tick = 0
        self._wrong_guesses
        print(self._word)
        for i in self._word:
            if i == self._let_guess:
                new_word.append(i)
                #print(i)

            else: 
                new_word.append('_')
                # self._wrong_guesses + 1
                # need to update so tick is given 1 if nothing is appended to the new_word then 
                # also need new_word to be the the result of the last terminal output
                #self._tick += 1
            


        return new_word, self._wrong_guesses
        

    


    
