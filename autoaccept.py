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

#pyautogui.displayMousePosition()

#def click(x,y):
#    pyautogui.click(x,y)
#    time.sleep(0.5)
#time.sleep(1)

# while True:
#     time.sleep(1)
#     if pyautogui.locateOnScreen("play_button.png"):
#         print("jest play")
#     else:
#         print("nie ma play")
        
