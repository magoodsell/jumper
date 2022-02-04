import random
class Word:
    def __init__(self):

        
        words = open('words.txt')
        self._get_word = random.choice(words)
        dashboard = [' '] * len(words)

        return self._get_word, dashboard



    
