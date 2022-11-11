# Words for the game
import random
from words import word_list

#This function handles the random choice of words from the wordslist
def start_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("I challenge you to NOT get hanged by the pole""/n""Good luck!")
    print(display_hangman(tries))
    print(word_completion)
    print("/n")
#While loop for handling the ammount of tries and when you´re out of guesses
    while not guessed and tries > 0 :
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Havent you clicked here before?", guess)
            elif guess not in word:
                print(guess, "its a good guess, but not the right one")
                tries  -= 1
                guessed_letters.append(guess)
            else:
                print("You are right!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)  
                if"_" not in word_completion: 
                    guess = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already clicked", guess)
            elif guess != word:
                print("the letter", guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("/n")
    if guessed:
        print("Youre a mastermind, you got the whole thing right! Well done! Up for another one?")
    else:
        print("How many tries left? thats right, NONE! Come back when you have looked in the dictionary! This word was " + word + "")
        
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
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
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = start_word()
    play(word)
    while input("Wanna go again? (Y for yes/N for No)").upper() == "Y":
        word = start_word()
        play (word)

if __name__ == "__main__":
    main()