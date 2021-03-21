#Word Games!
import random
import time


def fancyPrint(string, speed=10):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(1/(speed*10))
    print('')
    
def fancyInput(string, speed=10):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(1/(speed*10))
    return input('')

def guessTheNumber():
    playing = 1
    fancyPrint('Let\'s play a guesing game.')
    print('')
    while True:
        if not playing:
            break
        guessCount = 0
        lowerLimit = 1
        while True:
            difficulty = fancyInput('Choose your difficulty (easy, medium, hard, insane, custom):')
            difficulty = difficulty.lower()
            if difficulty == 'easy':
                upperLimit = 10
                break
            elif difficulty == 'medium':
                upperLimit = 100
                break
            elif difficulty == 'hard':
                upperLimit = 1000
                break
            elif difficulty == 'insane':
                upperLimit = 1000000
                break
            elif difficulty == 'custom':
                while True:
                    try:
                        lowerLimit = int(fancyInput('Enter the lowest possible number:'))
                        break
                    except:
                        fancyPrint('Sorry that\'s not a valid number.')
                while True:
                    try:
                        upperLimit = int(fancyInput('Enter the highest possible number:'))
                        break
                    except:
                        fancyPrint('Sorry that\'s not a valid number.')
                break
            else:
                fancyPrint('Invalid difficulty.')
                print('')
        setNum = random.randrange(lowerLimit, upperLimit+1)
        fancyPrint('I\'m thinking of a number between '+ str(lowerLimit) + ' and ' + str(upperLimit) + '.')
        guess = 0
        guessCount = []
        fancyPrint('Let\'s play!', 3)
        print('')
        while guess != setNum:
            while True:
                try:
                    guess = int(fancyInput('Guess a number:'))
                    break
                except:
                    fancyPrint('Sorry that\'s not a valid number.')
            if guess < setNum:
                fancyPrint('The number is higher than ' + str(guess))
                if guess in guessCount:
                    fancyPrint('You already guessed that btw.')
                elif guess < lowerLimit:
                    fancyPrint('Remember the number is higher than ' + str(lowerLimit -1))
                lowerLimit = guess + 1
                
            elif guess > setNum:
                fancyPrint('The number is lower than ' + str(guess))
                if guess in guessCount:
                    fancyPrint('You already guessed that btw.')
                elif guess > upperLimit:
                    fancyPrint('Remember the number is lower than ' + str(upperLimit+1))
                upperLimit = guess - 1
                
            if not guess in guessCount:
                guessCount.append(guess)
            print('')
        fancyPrint('Yeah it\'s ' + str(setNum) + '! Good job!')
        fancyPrint('You guessed it in ' + str(len(guessCount)) + ' tries.')
        print('')
        guessCOunt = 0
        guess = 0
        guessCOunt = []
        while True:
            playAgain = fancyInput('Do you want to play again? (Y/N):')
            playAgain = playAgain.lower()
            if playAgain == 'y':
                break
            elif playAgain == 'n':
                playing = 0
                break
            else:
                fancyPrint('Sorry, I don\'t understand.')
