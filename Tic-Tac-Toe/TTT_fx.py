import random


def display(board):
    print('\n' * 100)

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    game_is_running = True
    while game_is_running:
        options = ['X', 'O']
        marker = (input("Player1 choose an option: 'X' or 'O':\n\n")).upper()
        if marker not in options:
            print('You entered an incorrect option, try again\n')
            continue

        if marker == 'X':
            player1 = options[0]
            player2 = options[1]
        elif marker == 'O':
            player1 = options[1]
            player2 = options[0]
        else:
            continue

        print(f"\nplayer 1 is: '{player1}' \nplayer 2 is: '{player2}'\n")
        return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False


def choose_first():
    return random.choice(['heads', 'tails'])


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    while True:
        try:
            position = int(input('Enter a position using a number (1-9):\n'))
        except ValueError:
            display(board)
            print('Not a number')
            continue
        if position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if space_check(board, position):
                return position
            else:
                display(board)
                print('space already taken')
                continue
        else:
            display(board)
            print("Number not in the board's index range")
            continue


def replay():
    play_again = input('Do you want to play again? [y/n]\n').lower()
    if play_again == 'y':
        return True
    else:
        print("  THANK YOU FOR PLAYING :) ")


def ready():
    ask = input('   << Are you ready to play? [y/n] >>\n').lower()
    if ask == 'y':
        return True

