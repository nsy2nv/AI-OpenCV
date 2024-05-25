import cv2
import numpy as np
width = 720
height = 256
frameHSat = np.zeros([height,width,3], dtype = np.uint8)
frameHVal = np.zeros([height,width,3], dtype = np.uint8)
for i in range(0,height,1):
    for j in range(0,width,1):
        frameHSat[i,j]=(int(j/4),i,255)
frameHSat = cv2.cvtColor(frameHSat,cv2.COLOR_HSV2BGR)
print(frameHSat)
for row in range(0,height,1):
    for column in range(0,width,1):
        frameHVal[row,column] = (int(column/4),255,row)
frameHVal = cv2.cvtColor(frameHVal,cv2.COLOR_HSV2BGR)
print('HVal',frameHVal)
while True:
    cv2.imshow('HSaturation',frameHSat)
    cv2.moveWindow('HSaturation',0,0)
    
    cv2.imshow('HSValue',frameHVal)
    cv2.moveWindow('HSValue',0,height+40)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()