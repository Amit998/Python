import pyautogui
from PIL import Image,ImageGrab
import time
# from numpy import asarray
import numpy as np

def takeScreenShot():
    Image=ImageGrab.grab().convert('L')
    Image.show()
    return Image
if __name__=="__main__":
    print("Hey Dino Game Is About To started in 3 second")
    time.sleep(3)
    image=ImageGrab.grab().convert('L')
    data = image.load()
    

 
    for i in range(300,415):
        for j in range(600,660):
            data[i,j] =256 
    image.show() 
 

# 256 White
# 0 black
