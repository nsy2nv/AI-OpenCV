import cv2
import face_recognition as fr
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX

donFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/PythonAI/demoImages/known/Donald Trump.jpg')
faceLoc = fr.face_locations(donFace)[0]
print(faceLoc)
top, right, bottom, left = faceLoc
cv2.rectangle(donFace,(left,top),(right,bottom),(0,255,0),2)
donFaceBGR = cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR)
cv2.imshow('myWin', donFaceBGR)
cv2.waitKey(1000)
cam = cv2.VideoCapture()
#C:\\Users\\MTN-SIMREG\\AppData\\Local\\Microsoft\\WindowsApps\\python3.12.exe
print(np.__version__)