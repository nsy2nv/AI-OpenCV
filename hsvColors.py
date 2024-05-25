import cv2
import numpy as np
evt = 0
xPosition = 0
def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xPosition
    global yPosition
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        xPosition = xPos
        yPosition = yPos
    if event == cv2.EVENT_RBUTTONUP:
        evt = event
width = 720
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*'MJPG'))
cv2.namedWindow('myCam')
cv2.setMouseCallback('myCam',mouseClick)
while True:
    ignore, frame = cam.read()
    if evt == 1: # One is returned when the left mouse button is down
        pointIncam = np.zeros([250,250,3], dtype=np.uint8)
        y = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        camColor = y[yPosition][xPosition]
        pointIncam[:,:] = camColor
        cv2.putText(pointIncam,str(camColor),(10,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0))
        print(camColor)
        
        cv2.imshow('clickPoint',pointIncam)
        cv2.moveWindow('clickPoint',width,0)
        evt = 0
    if evt == 5:
        cv2.destroyWindow('clickPoint')
        evt = 0
    cv2.imshow('myCam', frame)
    cv2.moveWindow('myCam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()