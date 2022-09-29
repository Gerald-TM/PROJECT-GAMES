from TTT_fx import *

print('\nWelcome to TIC-TAC-TOE!!!\n')
board = [' '] * 10
board[0] = '#'
start = True
while start:
    player1_marker, player2_marker = player_input()
    coin = choose_first()
    if coin == 'heads':
        print('     << Player 1 is going first >>')
    else:
        print('     << Player 2 is going first >>')
    if ready():
        game_on = True
    else:
        print('Oh, bummer :(')
        break

    while game_on:
        if coin == 'heads':
            display(board)
            print(f"        << '{player1_marker}' make a move >>")
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display(board)
                print('     << Player 1 has won >>')
                game_on = False
            else:
                if full_board_check(board):
                    display(board)
                    print('Tie game')
                    game_on = False
                else:
                    coin = 'tails'
        else:
            display(board)
            print(f"        << '{player2_marker}' make a move >>")
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display(board)
                print('     << Player 2 has won >>')
                game_on = False
            else:
                if full_board_check(board):
                    display(board)
                    print('Tie game')
                    game_on = False
                else:
                    coin = 'heads'
    if replay():
        board = [' ']*10
        continue
    else:
        start = False