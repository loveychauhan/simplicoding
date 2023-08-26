import random


def guess(x):
    random_number = random.randint(1, x)
    guess= 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x} '))
        if guess < random_number:
            print("guess too low 📉")
        elif guess > random_number:
            print("guess too high 📈")

    print(f'yay u guess right number!! {guess}😍')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high:

        feedback = input(f'Is {guess} too high (H), is too low (L), or is correct (C)??_').lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1

    print(f'yay computer choose number correctly {guess} 😎')

computer_guess(100)








