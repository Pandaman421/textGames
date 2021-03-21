import time
import random
from guessNumber import *

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

def parseHighScores():
    return 0

games = [guessTheNumber]
fancyPrint('Welcome to Andrew\'s python text games!', 5)
fancyPrint('Here I have a wide variety of simple terminal based games for you!')
fancyPrint('Here\'s my collection!')
print('')

for index, game in enumerate(games):
    print(str(game.__name__) + ' : ' + str(index))
