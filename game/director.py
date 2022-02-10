from game.guess import Guess 
from game.terminal_service import terminal
from game.word import Word 


class Director:


    def __init__(self):

        self._word = Word()
        self._guess = Guess()
        self._terminal = terminal()
        self._is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            new_word = self._do_updates()
            self._do_outputs(new_word)

    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        # gets the actually word
        word = self._word.set_word()
        self._guess._word = word
        # gets the blank word
        blank_word = self._word.get_words()
        # displays the blank word
        self._terminal.display_word(blank_word)
        # passes the actually word to the guess class
        self._guess._word = word





    def _do_updates(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        # print parachute man
        self._terminal.results()

        # prompt the user for a guess
        letter = self._terminal.user_prompt()
        print(f'{letter}')
        print('h')
        # pass letter to the guess class
        self._guess._let_guess = letter
        # check for duplicates
        #self._guess.check_duplicate()
        # check if guess is correct
        new_word, wrong_count = self._guess.check_guess()

        return new_word

        


    def _do_outputs(self, new_word):
        """
        Args:
            self (Director): An instance of Director.
        """
        # display the new word 
        self._terminal.display_word(new_word)

        # display the parachut man
        self._terminal.results()

        self._word.new_word = new_word
        # end game
        # loop through the word new_word and check for _ is then _is_playing = True else False
        # and if failedguesses is == 4 then false 
        for i in self._word.display_word():
            if i == '_':
                self._is_playing = True 
            else:
                self._is_playing = False 

        if self._terminal._failedGuesses == 4:
            self._is_playing = False 


        

