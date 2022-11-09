# Words for the game
import random
from words import word_list


def start_word():
    word = random.choice(word_list)
    return word.upper()

