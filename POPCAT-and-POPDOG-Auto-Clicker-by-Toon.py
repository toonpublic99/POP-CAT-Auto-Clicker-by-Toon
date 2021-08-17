# POPCAT & POPDOG Auto Clicker by Toon, Version 1.2.2

import pyautogui
import keyboard
import time

def printFunction():
    print('Guide: You can input 2 command and 1 press on your keyboard\n'
          '- Input the "start" command to click\n'
          '- Input the "exit" command to leave\n'
          '- Press the "Esc" button to stop')

try:
    print('POPCAT & POPDOG Auto Clicker by Toon, Version 1.2.2\n'
          '---------------------------------------------')
    printFunction()

    input1 : str
    input1 = 'xxxxx'

    while input1 != 'start':
        input1 = str(input('\n\nInput >>  '))
        if input1 == 'start':
            while input1 == 'start':
                    points = ['!', '!', '!', '!', '!', '!', '!', '!', '!', '!']
                    print('[', end=' ')
                    for x in points:
                        print(x, end=' ')
                        time.sleep(0.5)
                    print(']')
                    while input1 == 'start':
                        x, y = pyautogui.position()
                        myPosition = x, y
                        pyautogui.doubleClick(myPosition)
                        if keyboard.is_pressed('esc'):
                            input1 = str(input('\nInput >>  '))
                            if input1 == 'exit':
                                exit()
                            elif input1 == 'start':
                                print('[', end=' ')
                                for x in points:
                                    print(x, end=' ')
                                    time.sleep(0.5)
                                print(']')
                                continue
                            else:
                                print('Incorrect Command: Please Input Again !\n')
                                printFunction()
                                continue
        elif input1 == 'exit':
            exit()
        else:
            print('Incorrect Command: Please Input Again !\n')
            printFunction()
            continue
except KeyboardInterrupt:
    print('\nDone')
