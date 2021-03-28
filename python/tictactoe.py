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
    
    #first we check each row
    for row in range(board[0]):
        tempArray = board[(board[0]*row)+1:(board[0]*row)+1+board[0]]
        if all(elem == tempArray[0] for elem in tempArray):
            return(tempArray[0])
        
    #Then each column
    for column in range(board[0]):
        tempArray = []
        for num in range(board[0]):
            tempArray.append(board[1+column+(num*board[0])])
        if all(elem == tempArray[0] for elem in tempArray):
            return(tempArray[0])
        
    #Now the diagonals
    diagonal = []
    for num in range(board[0]):
        diagonal.append(board[1+num*(1+board[0])])
    if all(elem == tempArray[0] for elem in tempArray):
        return(tempArray[0])
    
    diagonal = []
    for num in range(board[0]):
        diagonal.append(board[0]+(num*(board[0]-1)))
    if all(elem == tempArray[0] for elem in tempArray):
        return(tempArray[0])
    
    #Now check for a cat
    
    for num in board[1:]:
        if type(num) == int:
            break
def tictactoe():
    fancyPrint('Let\'s play some tic tac toe.')
    board = makeBoard(3)
    while True:
        gameMode = input('How many people are playing? (1/2):')
        if gameMode == '1' or gameMode == '2':
            gameMode = int(gameMode)
            break
        else:
            print('Invalid Number of players.')
    
    print('Let\s flip a coin to see who goes first.')
    print('')
    turn = random.randrange(0,2)
    while True:
        if turn:
            if gameMode == 1:
                print('Your turn!')
            if gameMode == 2:
                print('Player one\'s turn.')
            while turn:
                printBoard(board)
                try:
                    spot = int(input('Pick a spot:'))
                    if spot in(board[1:]):
                        board[spot] = 'x'
                        turn = 0
                    else:
                        print('Sorry that spot is not available.')
                except:
                    print('Sorry that\'s not a valid input.')
                print('')
        else:
            if gameMode == 1:
                print('Ok my turn.')
                while not turn:
                    AIturn = random.randrange(1, len(board))
                    if board[AIturn] == AIturn:
                        board[AIturn] = 'o'
                        turn = 1
            if gameMode == 2:
                print('Player two\'s turn.')
                while not turn:
                    printBoard(board)
                    try:
                        spot = int(input('Pick a spot:'))
                        if spot in(board[1:]):
                            board[spot] = 'o'
                            turn = 0
                        else:
                            print('Sorry that spot is not available.')
                    except:
                        print('Sorry that\'s not a valid input.')
                    print('')
        if checkBoard(board) == 'x':
            if gamemode == 1:
                print('Gongrats, you win!')
                break
            if gameMode == 2:
                print('Player 1 wins!')
                break
        if checkBoard(board) == 'o':
            if gameMode == 1:
                print('Haha, looks like I wil this one.')
                break
            if gameMode == 2:
                print('Player 2 wins!')
                break
        if checkBoard(board) == 'cat':
            print('Looks like we got a draw.')
            break