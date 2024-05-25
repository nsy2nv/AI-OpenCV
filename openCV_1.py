
import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam1', frame)
    cv2.imshow('webcam2', grayFrame)
    cv2.imshow('webcam3', grayFrame)
    cv2.imshow('webcam4', frame)
    cv2.moveWindow('webcam1',0,0)
    cv2.moveWindow('webcam2',640,0)
    cv2.moveWindow('webcam3',0,400)
    cv2.moveWindow('webcam4',640,400)
    
    cv2.resizeWindow('webcam1', width=640, height=400)
    cv2.resizeWindow('webcam2', width=640, height=400)
    cv2.resizeWindow('webcam3', width=640, height=400)
    cv2.resizeWindow('webcam4', width=640, height=400)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()