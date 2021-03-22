from guessNumber import fancyPrint, fancyInput
import random

board = [
        [1, 2, 3, 5, 6, 2, 4],
        [4, 5, 6, 3, 4, 3, 7],
        [7, 8, 9, 2, 5, 2, 9],
    ]

def printboard(board):
    height = len(board)
    width = len(board[0])
    for row, y in enumerate(board):
        
        for space in range(width):
            if space != 0:
                print('|', end='')
            print('     ', end='')
        print('')
        
        for column, x in enumerate(y):
            
            if column != 0:
                print('|', end='')
            print('  ' + str(x) + '  ', end='')
        print('')

        for space in range(width):
            if space != 0:
                print('|', end='')
            if row != height-1:
                print('_____', end='')
            else:
                print('     ', end='')
        print('')
        

        
def tictactoe():
    fancyPrint('Let\'s play some tic tac toe.')
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print('Let\s flip a coin to see who goes first.')
    myturn = random.randrange(0,2)

printboard(board)
