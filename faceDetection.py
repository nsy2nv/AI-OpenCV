import cv2
import time
width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/PythonAI/haar/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/PythonAI/haar/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/PythonAI/haar/haarcascade_smile.xml')
startTime = time.time()
fps = 10
fpsFilt = 10
while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Detect face and two eyes
    faces = faceCascade.detectMultiScale(frameGray, 1.3,5)
    for face in faces:
        xPos,yPos,widt,heit = face
        cv2.rectangle(frame,(xPos,yPos),(xPos+widt,yPos+heit),(0,255,0),2)
        frameROI = frame[yPos:yPos+heit,xPos:xPos+widt]
        frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(frameROIGray)
        for eye in eyes:
            xEye,yEye,widtEye,heitEye = eye
            cv2.rectangle(frameROI,(xEye,yEye),(xEye+widtEye,yEye+heitEye),(0,0,255),2)
        smiles = smileCascade.detectMultiScale(frameROIGray)
        for smile in smiles:
            x,y,w,h = smile
            cv2.rectangle(frameROI,(x,y),(x+w,y+h),(255,0,0),2)

    timeLoop = time.time() - startTime
    fps = 1/timeLoop
    fpsFilt = .90*fpsFilt + .10*fps
    print(int(fpsFilt))
    startTime = time.time()
    cv2.imshow('myWin',frame)
    cv2.moveWindow('myWin',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release