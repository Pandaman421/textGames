from guessNumber import fancyPrint, fancyInput
import random
import math

def makeBoard(size):
    board = []
    board.append(size)
    for i in range(size**2):
        board.append(i+1)
    return board

def printBoard(board):
    height = len(board)
    width = len(board)
    for y in range(board[0]):
        for space in range(board[0]):
            if space != 0:
                print('|', end='')
            print('     ', end='')
        print('')
        
        for char in range(board[0]):
            if char != 0:
                print('|', end='')
            print('  ' + str(board[1+(y*board[0])+char]) + '  ', end='')
        print('')

        for space in range(board[0]):
            if space != 0:
                print('|', end='')
            if y != board[0]-1:
                print('_____', end='')
            else:
                print('     ', end='')
        print('')

testBoard = [3, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def checkBoard(board):
    #this will check and return a 'o' if o wins, and a 'x' if x wins.
    for y, rows in enumerate(board):
        comparison = board[(y*board[0]) + 1]
        counter = 0
        for x, character in enumerate(board):
            if character == [(y*board[0]) + x + 1]:
                counter += 1
        if counter == board[0]:
            return(comparison)
def tictactoe():
    fancyPrint('Let\'s play some tic tac toe.')
    board = makeBoard(3)
    availableSpaces = []
    
    print('Let\s flip a coin to see who goes first.')
    myturn = random.randrange(0,2)
    while True:
        if myturn == 0:
            return(7)


print(checkBoard(testBoard))