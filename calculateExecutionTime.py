import cv2
import time
print(cv2.__version__)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width = 720
height = 360
myRadius = 30

topLeftCorner = (240,120)
downRightCorner = (400,320)
greenColor = (0,255,0)
blackColor = (0,0,0)
fontType = cv2.FONT_HERSHEY_COMPLEX_SMALL
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 10)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*'MJPG'))
tLast = time.time()
fpsFilt = 10
time.sleep(.01)
while True:
    dT = time.time()-tLast
    fps = 1/dT
    #Frequency filter help to smoothen the changes in frequencies
    fpsFilt = fpsFilt*.80 + fps*.20
    print(fpsFilt)

    tLast = time.time()
    ignore, frame = cam.read()
    #Big centered for facial detection
    cv2.rectangle(frame,topLeftCorner,downRightCorner,greenColor,2)
    #Top left corner for timestame
    cv2.rectangle(frame,(0,0),(140,40),(0,0,0),-2)
    cv2.putText(frame,str(int(fpsFilt))+' fps',(6,20),fontType,1,(255,255,255),1)
    #cv2.circle(frame,(320,180),myRadius, (0,0,255), 2)
    #frame[120:240,320:400] = [0,0,0]
    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()