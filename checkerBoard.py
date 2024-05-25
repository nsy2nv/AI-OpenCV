import cv2
import numpy as np
print(cv2.__version__)

while True:
    frame = np.zeros([600,800,3], dtype=np.uint8)
    rows = int(600/8)
    columns = int(800/8)
    
    for i in range(0, 8):
        for j in range(0, 8):
            frame[0:rows,columns:columns*2] = [0,0,255]
            frame[0:rows,columns*3:columns*4] = [0,0,255]
            frame[0:rows,columns*5:columns*6] = [0,0,255]
            frame[0:rows,columns*7:columns*8] = [0,0,255]

            frame[rows:rows*2,0:columns] = [0,0,255]
            frame[rows:rows*2,columns*2:columns*3] = [0,0,255]
            frame[rows:rows*2,columns*4:columns*5] = [0,0,255]
            frame[rows:rows*2,columns*6:columns*7] = [0,0,255]

            frame[rows*2:rows*3,columns:columns*2] = [0,0,255]
            frame[rows*2:rows*3,columns*3:columns*4] = [0,0,255]
            frame[rows*2:rows*3,columns*5:columns*6] = [0,0,255]
            frame[rows*2:rows*3,columns*7:columns*8] = [0,0,255]

            frame[rows*3:rows*4,0:columns] = [0,0,255]
            frame[rows*3:rows*4,columns*2:columns*3] = [0,0,255]
            frame[rows*3:rows*4,columns*4:columns*5] = [0,0,255]
            frame[rows*3:rows*4,columns*6:columns*7] = [0,0,255]



    cv2.imshow('Image', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break