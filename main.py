import pyautogui
from PIL import Image,ImageGrab
import time
# from numpy import asarray
import numpy as np
# con =True
def hit(data):
    pyautogui.keyDown('space')

# def draw():
          
def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 300):
        for j in range(470, 563):
            if data[i, j] > 128:
                hit("down")
                return True

    for i in range(350, 415):
        for j in range(603, 650):
            if data[i, j] > 128:
                hit("up")
                return True
    return False


# pyautogui.keyDown('hh')
# def takeScreenShot():
#     Image=ImageGrab.grab().convert('L')
#     Image.show()
#     return Image


if __name__=="__main__":
    print("Hey Dino Game Is About To started in 3 second")
    # con = True 
    time.sleep(3)
    # hit('up')
    while True:
        image=ImageGrab.grab().convert('L')
        data = image.load()
    
        # print(np.asarray(image))
        # if isCollide(data):
        #     hit('up')
        isCollide(data)
       
 
    # # Draw the rectangle for cactus
    #     for i in range(300, 415):
    #         for j in range(563, 650):
    #             data[i, j] = 0
        
    #     # Draw the rectangle for birds
    #     for i in range(250, 300):
    #         for j in range(410, 563):
    #             data[i, j] = 256
    # con = False

# 256 White
# 0 black
