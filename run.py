# Words for the game

import random
from words import word_list

# This function handles the random choice of words from the wordslist


def start_word():
    word = random.choice(word_list)
    return word.upper()


# This function handles the games structure, lives and startup text


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("I challenge you to NOT get hanged by the pole"
          "\n"
          "Good luck!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

# This is a while loop for handling the ammount of
# tries and when you´re out of guesses
# cred to Kaleb from kite for making this a less mess to me

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Havent you clicked here before?", guess)
            elif guess not in word:
                print(guess, "is a good guess, but not the right one")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("You are right!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
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
        print("\n")

    if guessed:

        print("You´re a mastermind, you got the whole thing right!"
              "\n"
              "Well done! "
              "\n"
              "Up for another one?")
    else:
        print("How many tries left? thats right, NONE!"
              "\n"
              "Come back when you´ve looked in the dictionary!"
              "\n"
              "This word was " + word + "")


# This section is the diffrent graphics when you guess wrong
# It´s seven diffrent stages that represent the 7 lives


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, both legs and dead face
                """
                   --------
                   |      |
                   |    (x.x)
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, body, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, body, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and body
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


# This funtion handles the restart/ retry


def main():
    word = start_word()
    play(word)
    while input("Wanna go again? (Y for yes/N for No)").upper() == "Y":
        word = start_word()
        play(word)


if __name__ == "__main__":
    main()
