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
                print(guess, "it´s a good guess, but not the right one")
                tries  -= 1
                guessed_letters.append(guess)
            else:
                print("You are right!" guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completiton)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completiton = "".join(word_as_list)  
                if"_" not in word_completiton: 
                    guess = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already clicked", guess)
            elif guess != word:
                print("the letter" guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completiton = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completiton)
        print("/n")
    if guessed:
        print("You´re a mastermind, you got the whole thing right! Well done! Up for another one?")
    else:
        print("How many tries left? that´s right, NONE! Come back when you looked in the dictionary!")
        
def display_hangman(tries):
    stages = [  
                #final state, head, torso, both arms, both legs and dead-face
                """
                   --------
                   |      |   
                   |    (x.x) 
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        
        
                #head, torso, both arms, and both legs
                """
                   --------
                   |      |    
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Wanna go again? (Y for yes/N for No)").upper() == "Y":
        word = get_word()
        play (word)
        

    
            