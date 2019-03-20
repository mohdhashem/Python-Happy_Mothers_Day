import os
import time
from random import randint
from colorama import init, Fore, Back, Style

init(convert=True)

os.system("C:\\Users\\m7ama\\source\\repos\\pyProject\\pyProject\\music_Mom.bat")

for i in range(1,45):
    print('')

heartStars = [2,4,8,10,14,20,26,28,40,44,52,60,64,76]
heartBreakLines = [13,27,41,55,69,77]

red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT

def addSpaces(a):
    count = a
    while count > 0:
        print(' ', end='')
        count -= 1

def newLineWithSleep():
    time.sleep(0.3)
    print('\n', end='')

play = 0
while play == 0:
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
            
    for i in range(0,78):
        if i in heartBreakLines:
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in heartStars:
            print(red + '*', end='')
        elif i in (32,36):
            print(green + 'M', end='')
        elif i == 34:
            print(green + 'O', end='')
        else:
            print(' ', end='')

    newLineWithSleep()
    addSpaces(randint(8, 80))
    print(cyan + "H a p p y  M o t h e r ' s   D a y !", end='')
    newLineWithSleep()
    newLineWithSleep()

    flowerBreakLines = [7,15,23,31,39,46]
        
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,47):
        if i in flowerBreakLines:
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (2,8,12,18):
            print(magenta + '{', end='')
        elif i in (3,9,13,19):
            print(magenta + '_', end='')
        elif i in (4,10,14,20):
            print(magenta + '}', end='')
        elif i in (27,35,43):
            print(green + '|', end='')
        elif i in (34,44):
            print(green + '~', end='')
        elif i == 11:
            print(yellow + 'o', end='')
        else:
            print(' ', end='')

    print('\n', end='') # By Mohammad Hashem
