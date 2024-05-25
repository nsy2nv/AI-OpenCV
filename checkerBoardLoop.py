import cv2
import numpy as np
print(cv2.__version__)

boardSize = int(input('Enter the size of the board '))
num_of_block = int(input('How many block would you like? '))
squareSize = int(boardSize/num_of_block)
darkColor = (0,0,0)
brightColor =(0,0,255)
currentColor = darkColor
while True:
    frame = np.zeros([boardSize,boardSize,3], dtype=np.uint8)
    
    
    for row in range(0, num_of_block):
        for column in range(0, num_of_block):
            frame[squareSize*(row):squareSize*(row+1),squareSize*(column):squareSize*(column+1)] = currentColor
            if currentColor == darkColor:
                currentColor = brightColor
            else:
                currentColor = darkColor
        if  currentColor == darkColor:
            currentColor = brightColor
        else:
            currentColor = darkColor
  
    cv2.imshow('Image', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break