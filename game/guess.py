import word



class Guess:
    """
    The responsibility of the guess is to take the user guess and update the word. It will pass the
    word to the terminal and keep track of the number of wrong guesses. 

    Attributes: 

    """


    def __init__(self):
        """Constructs a new guess.
        
        Args:
            self (Guess): an instance of Guess.
        """

        self._guess = ''
        self._word = word.get_word() # it should probably be _set_word will have to add this to the game.
        self._all_guesses = []

        pass 

    def get_guess(self):
        """
        Purpose is to get the word the person has guessed and append to _all_guesses
        """
        return self._all_guesses.append(self._guess)

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
        for i in len(self._word):
            if i == self._guess:
                new_word.append(i)
            else: 
                new_word.append('_')

        return new_word 
        

    


    
