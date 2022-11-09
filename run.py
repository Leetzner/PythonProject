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
    print("I challenge you to NOT get hanged by the pole""/n""Good luck!")
    print(display_hangman(tries))
    print(word_completiton)
    print("/n")
#While loop for handling the ammount of tries and when you´re out of guesses
    while not guessed and tried > 0 :
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Haven´t you clicked here before?", guess)
            elif guess not in word:
                print(guess, "is a good guess, but not the right one")
                tries  -= 1
                guessed_letters.append(guess)
            else:
                print("Good job",guess, "is in the word!")
                guessed_letters.append(guess)
                word as list = list(word_completiton)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
        

    
            