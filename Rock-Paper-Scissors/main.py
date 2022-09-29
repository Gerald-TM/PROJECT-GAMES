import random

print()
print('Welcome to The [Rock-Paper-Scissors] Game!!!')
print()

while True:
    # Game options
    options = ['R', 'P', 'S']

    # User input
    Player = input('Pick an option: Rock (R), Paper (P), or Scissors (S) : ').upper()

    # CPU's choice
    CPU = random.choice(options)

    # Validation of user input
    if Player not in options:
        print()
        print('                [ERROR] \n --Input NOT amongst options. Try again--')
        print()
    else:
        print()
        print('Player', '(', Player, ')', ':', 'CPU', '(', CPU, ')')
        print()

    # For Tie
    if Player == CPU:
        print('         Tie!!!')
        print()

    # Rock
    if Player == 'R' and CPU == 'S':
        print('Rock beats Scissors')
        print('    You Win!!!')
        break
    if Player == 'R' and CPU == 'P':
        print('Paper beats Rock')
        print('   CPU Wins\n   You Lose.')
        break

    # Paper
    if Player == 'P' and CPU == 'R':
        print('Paper beats Rock')
        print('  You Win!!!')
        break
    if Player == 'P' and CPU == 'S':
        print('Scissors beats Paper')
        print('     CPU Wins\n     You Lose.')
        break

    # Scissors
    if Player == 'S' and CPU == 'P':
        print('Scissors beats Paper')
        print('    You Win!!!')
        break
    if Player == 'S' and CPU == 'R':
        print('Rock beats Scissors')
        print('     CPU Wins\n     You Lose.')
        break

    continue


# End of game
print()
print('Thanks for playing')
