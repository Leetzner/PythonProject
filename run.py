# Words for the game
import random
from words import word_list

def start_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completiton="_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7