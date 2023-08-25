import random

from words import words

print("welcome to HANGMAN")   # intro
print("_______________________________\n")

randomwords = random.choice(words)

for x in randomwords:  # printing number of character to guess?
    print('_', end=' ')


def hangman(wrong):   # drawing hangman
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")

    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")

    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")

    elif wrong == 3:
        print("\n +---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===")

    elif wrong == 4:
        print("\n +---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")

    elif wrong == 5:
        print("\n +---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")

    elif wrong == 6:
        print("\n +---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


def print_lines():  # optional___some line for clean look
    print("\r")
    for char in randomwords:
        print("\u203E", end=" ")


def printing_letter(guessedword):   # printing the word guessed by user
    counter = 0
    right_word = 0
    for char in randomwords:
        if char in guessedword:
            print(randomwords[counter], end=" ")
            right_word += 1

        else:
            print(" ", end=" ")

        counter += 1

    return right_word  # to check the while loop


length_of_random_word = len(randomwords)   # variables
wrong_guesses = 0
correct_guesses = 0
user_letter_guess = []

# run condition
while wrong_guesses != 6 and length_of_random_word != correct_guesses:
    print("\nletter guessed so far: ")
    for letter in user_letter_guess:
        print(letter, end=" ")

    letter_guessed = input("\nguess a letter: ")
    # if user guessed right letter
    if letter_guessed in randomwords:
        hangman(wrong_guesses)
        user_letter_guess.append(letter_guessed)
        correct_guesses = printing_letter(user_letter_guess)
        print_lines()
    # if user guessed wrong letter
    else:
        wrong_guesses += 1
        user_letter_guess.append(letter_guessed)
        hangman(wrong_guesses)
        correct_guesses = printing_letter(user_letter_guess)
        print_lines()
    # end line
print("\ngame over :)")
