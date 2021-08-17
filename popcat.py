import pyautogui
import keyboard


try:
    print('POPCAT Auto Clicker by Toon\nVersion 1.0.0\nHow to use it?\n'
          'The steps for using are as follows:\nStep 1: Move '
          'your mouse to the cat\nStep 2: The program will process\nStep 3: '
          'If you want to stop, you can press the "Esc" button on your keyboard')
    while True:
        x, y = pyautogui.position()
        myPosition = x, y
        pyautogui.click(myPosition)
        if keyboard.is_pressed('esc'):
            break
except KeyboardInterrupt:
    print('\nDone')
