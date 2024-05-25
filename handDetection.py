import cv2
import mediapipe as mp
width = 640
height = 360
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))
hands = mp.solutions.hands.Hands(False,2)
myDraw = mp.solutions.drawing_utils
while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    print(results)
    if results.multi_hand_landmarks != None:
        myHands = []
        for handLandMarks in results.multi_hand_landmarks:
            myHand = []
            myDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for Landmark in handLandMarks.landmark:
                #Unnormalise the x,y values by multiplying it with width and height
                myHand.append((int(Landmark.x*width),int(Landmark.y*height)))
            myHands.append(myHand)
            print(myHands)
            cv2.circle(frame,myHand[8],7,(255,255,100),-1)
            print('')
    cv2.imshow('myWin',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()