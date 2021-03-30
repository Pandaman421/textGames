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
    print('')

testBoard = [3, 'o', 2, 'o', 4, 'o', 6, 'o', 8, 'o']

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
    if all(elem == diagonal[0] for elem in diagonal):
        return(diagonal[0])
    
    diagonal = []
    for num in range(board[0]):
        diagonal.append(board[0]+(num*(board[0]-1)))
    if all(elem == diagonal[0] for elem in diagonal):
        return(diagonal[0])
    
    #Now check for a cat
    cat = 1
    for num in board[1:]:
        if num != 'o' and num != 'x':
            cat = 0
    if cat:
        return 'cat'
    
def tictactoe():
    playing = 1
    while playing:
        fancyPrint('Let\'s play some tic tac toe.')
        board = makeBoard(3)
        while True:
            gameMode = fancyInput('How many people are playing? (1/2):')
            if gameMode == '1' or gameMode == '2':
                gameMode = int(gameMode)
                break
            else:
                print('Invalid Number of players.')
        
        printBoard(board)
        fancyPrint('Let\s flip a coin to see who goes first.')
        fancyPrint('. . . ', 1)
        print('')
        turn = random.randrange(0,2)
        while True:
            if checkBoard(board) == 'x':
                if gameMode == 1:
                    fancyPrint('Gongrats, you win!')
                    break
                if gameMode == 2:
                    fancyPrint('Player 1 wins!')
                    break
            if checkBoard(board) == 'o':
                if gameMode == 1:
                    fancyPrint('Haha, looks like I win this one.')
                    break
                if gameMode == 2:
                    fancyPrint('Player 2 wins!')
                    break
            if checkBoard(board) == 'cat':
                fancyPrint('Looks like we got a draw.')
                break
            
            if turn:
                if gameMode == 1:
                    fancyPrint('Your turn!')
                if gameMode == 2:
                    fancyPrint('Player one\'s turn.')
                while turn:
                    try:
                        spot = int(fancyInput('Pick a spot:'))
                        if spot in(board[1:]):
                            board[spot] = 'x'
                            turn = 0
                        else:
                            fancyPrint('Sorry that spot is not available.')
                            printBoard(board)
                    except:
                        fancyPrint('Sorry that\'s not a valid input.')
                        printBoard(board)
                    print('')
                printBoard(board)
            else:
                if gameMode == 1:
                    fancyPrint('Ok my turn.')
                    while not turn:
                        AIturn = random.randrange(1, len(board))
                        if board[AIturn] == AIturn:
                            board[AIturn] = 'o'
                            turn = 1
                    printBoard(board)
                if gameMode == 2:
                    fancyPrint('Player two\'s turn.')
                    while not turn:
                        try:
                            spot = int(fancyInput('Pick a spot:'))
                            if spot in(board[1:]):
                                board[spot] = 'o'
                                turn = 0
                            else:
                                fancyPrint('Sorry that spot is not available.')
                                printBoard(board)
                        except:
                            fancyPrint('Sorry that\'s not a valid input.')
                            printBoard(board)
                        print('')
                    printBoard(board)
        while True:
            playAgain = fancyInput('Would you like to play again? (y/n):')
            playAgaion = playAgain.lower()
            if playAgain == 'y' or playAgain == 'yes':
                break
            elif playAgain == 'n' or playAgain == 'no':
                playing = 0
                break
            else:
                fancyPrint('Sorry that is not a valid input.')
        print('')




tictactoe()