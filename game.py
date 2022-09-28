import random
turns = ['rock', 'paper', 'scissors']
human_turn = input('Enter your turn, or type exit: ')
computer_turn = random.choice(turns)


while(True):
    print(f'Human:{human_turn} vs. computer: {computer_turn}')
    if human_turn == computer_turn:
        if human_turn == 'exit':
            break
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
    else:
        print('Computer wins!')
