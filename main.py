import random


def play():
    player = input("input 'r' for rock, 's' for scissor and 'p' for paper ").lower()
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        print("its a draw try again ")

    print(is_win(player, computer))


def is_win(player, computer):

    if (player == 'r') or (player == 'p') or (player == 's'):

        if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (
                player == 'p' and computer == 'r'):
            return 'you win computer chooses ' + computer

        elif (player == 'r' and computer == 'p') or (player == 's' and computer == 'r') or \
                (player == 'p' and computer == 's'):
            return "you loose  computer chooses " + computer

    else:
        return 'choose wisely'


play()
