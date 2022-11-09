# Words for the game
import random
from words import word_list

#This function handles the random choice of words from the wordslist
def start_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completiton="_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("I challenge you to not get hanged by the pole")
    print(display_hangman(tries))
    print(word_completiton)
    print("/n")
    while not guessed and tried > 0 :
        guess = input("Please guess a letter or word:").upper()