import cv2
width = 640
height = 360
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands = 2):
        self.hands = self.mp.solutions.hands.Hands(False,maxHands)
    def Marks(self,frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for LandMarks in handLandMarks.landmark:
                    myHand.append((int(LandMarks.x*width),int(LandMarks.y*height)))
                myHands.append(myHand)
        return myHands
paddleWidth  = 125
paddleHeight = 25
paddleColor = (0,255,0)

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))
findHands = mpHands()
while True:
    ignore,frame = cam.read()
    handData = findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)
    cv2.imshow('myWin',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
