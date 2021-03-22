import random
from guessNumber import *
from printText import *

'''
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
'''

def parseHighScores():
    return 0

games = [guessTheNumber]
fancyPrint('Welcome to Andrew\'s python text games!', 5)
fancyPrint('Here I have a wide variety of simple terminal based games for you!')
print('')
fancyPrint('Here\'s my collection!')
while True:
    for index, game in enumerate(games):
        fancyPrint(str(game.__name__) + ' : ' + str(index))
    fancyPrint('\'q\' to quit')
    choice = fancyInput('Which would you like to play?:')
    print('')
    try:
        choice = int(choice)
        games[choice]()
    except:
        choice = choice.lower()
        if choice == 'quit' or choice == 'q':
            break
        else:
            fancyPrint('Sorry I don\'t have that game.')
            print('')

fancyPrint('Ok Hopefully I\'ll see you soon!')
fancyInput('press enter to quit.')
