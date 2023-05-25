import time
import pyautogui
from python_imagesearch.imagesearch import imagesearch

accept_button = './accept_button.png'
play_button = './play_button.png'

def checkGame():
    while True:
        position = imagesearch(accept_button.png, 0.9)
        if not position[0] == -1:
            pyautogui.click(position[0], position[1])
            print("Game accepted")
            break

        time.sleep(1)
        
def main():
    run = True
    while run is True:
        checkGame()
        break

if __name__ == '__main__':
    print("Running")
    main()
