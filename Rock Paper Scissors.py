import random

def play():
    user = input("Choose one of the following: 'R' for Rock, 'P' for paper, 'S' for scissors ")
    computer = random.choice(['r', 'p' , 's'])

    if user == computer:
        return 'It is a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost'

def is_win(user, computer):

    if (user == 'r' and computer == 's') or (user =='s' and computer =='p') or (user == 'p' and computer == 'r'):
        return True

print(play())