import cv2
import numpy as np

def hueHighFunc(val):
    global hueHigh
    hueHigh = val
    print('hue High',hueHigh)

def hueLowFunc(val):
    global hueLow
    hueLow = val
    print('hue Low',hueLow)

def satHighFunc(val):
    global satHigh
    satHigh = val
    print('sat High',satHigh)

def satLowFunc(val):
    global satLow
    satLow = val
    print('sat Low',satLow)

def valHighFunc(val):
    global valHigh
    valHigh = val
    print('val High',valHigh)

def valLowFunc(val):
    global valLow
    valLow = val
    print('val Low ',valLow)
def hueLow2rdColor(val):
    global hueLow2rd
    hueLow2rd = val
    print('Hue Low2rd ',hueLow2rd)
def hueHigh2rdColor(val):
    global hueHigh2rd
    hueHigh2rd = val
    print('Hue high2rd ',hueHigh2rd)
hueHigh = 179
hueLow = 0
satHigh = 255
satLow = 0
valHigh = 255
valLow = 0
hueLow2rd = 0
hueHigh2rd = 179

width = 720
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))
cv2.namedWindow('myTrackBar')
cv2.resizeWindow('myTrackBar',400,300)
cv2.moveWindow('myTrackBar',width,0)
cv2.createTrackbar('Hue Low','myTrackBar',10,179,hueLowFunc)
cv2.createTrackbar('Hue High','myTrackBar',40,179,hueHighFunc)
cv2.createTrackbar('Hue Low2rd','myTrackBar',10,179,hueLow2rdColor)
cv2.createTrackbar('Hue High2rd','myTrackBar',40,179,hueHigh2rdColor)
cv2.createTrackbar('Sat Low','myTrackBar',10,255,satLowFunc)
cv2.createTrackbar('Sat High','myTrackBar',150,255,satHighFunc)
cv2.createTrackbar('Val Low','myTrackBar',50,255,valLowFunc)
cv2.createTrackbar('Val High','myTrackBar',150,255,valHighFunc)

while True:
    ignore,frame = cam.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow,satLow,valLow])
    upperBound = np.array([hueHigh,satHigh,valHigh])

    lowerBound2 = np.array([hueLow2rd,satLow,valLow])
    upperBound2 = np.array([hueHigh2rd,satHigh,valHigh])

    myMask = cv2.inRange(frameHSV,lowerBound,upperBound)
    myMask2 = cv2.inRange(frameHSV,lowerBound2,upperBound2)
    contours, junk = cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,0,255,3))

    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= 200:
            #cv2.drawContours(frame,[contour],-1,(0,0,255,3))
            xPos,yPos,wth,hgt = cv2.boundingRect(contour)
            cv2.rectangle(frame,(xPos,yPos),(xPos+wth,yPos+hgt),(0,255,0),3)

    #myMaskComp = myMask | myMask2
    myMaskComp = cv2.add(myMask,myMask2)
    myObject = cv2.bitwise_and(frame,frame,mask=myMaskComp)
    myObjectSmall = cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('My Object', myObjectSmall)
    cv2.moveWindow('My Object',int(width/2),height)

    myObjectSmall2 = cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow('My Object 2', myObjectSmall2)
    cv2.moveWindow('My Object 2',0,height+int(height/2)+30)

    cv2.imshow('My Mask',myMask)
    cv2.moveWindow('My Mask',0,height)
    cv2.resizeWindow('My Mask',int(width/2),int(height/2))
    cv2.imshow('window',frame)
    cv2.moveWindow('window',xPos,yPos)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release