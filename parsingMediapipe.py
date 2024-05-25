class HandLandMarkData:
    global width 
    global height
    width = 640
    height = 360

    def parseMediapipe():
        import mediapipe as mp
        hands = mp.solutions.hands.Hands(False,2)
        myDraw = mp.solutions.drawing_utils
        results = hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            myHands = []
            for handLandMarks in results.multi_hand_landmarks:
                myHand  = []
                myDraw.draw_landmarks(frame,handLandMarks)
                for LandMark in handLandMarks.landmark:
                    myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
                myHands.append(myHand)
                print(myHands)
                print('')
        
import cv2
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    HandLandMarkData.parseMediapipe()
    cv2.imshow('myWin',frame)
    if cv2.waitKey(1)&0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
