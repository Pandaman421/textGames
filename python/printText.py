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
