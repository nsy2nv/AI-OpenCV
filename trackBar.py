import cv2
def xTrackBar(val):
    global xPos
    xPos = val
    print('xPos ',val)
def yTrackBar(val):
    global yPos
    yPos = val
    print('yPos ',val)
def myRadTrackBar(val):
    global myRadius
    myRadius = val
def myMoveWinXTrackBar(val):
    global myMoveWinX
    myMoveWinX = val
def myMoveWinYTrackBar(val):
    global myMoveWinY
    myMoveWinY = val
def myNewWinSize(val):
    width = val
    height = int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

width = 720
height = 360
myRadius = 1
myMoveWinX = 0
myMoveWinY = 0
newWidth = 0
newHeight = 0
xPos = int(width/2)
yPos = int(height/2)
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))
cv2.namedWindow('myTrackBars')
cv2.resizeWindow('myTrackBars',400,250)
cv2.moveWindow('myTrackBars',950,0)
cv2.createTrackbar('xPos','myTrackBars',0,width,xTrackBar)
cv2.createTrackbar('yPos','myTrackBars',0,height,yTrackBar)
cv2.createTrackbar('myRad', 'myTrackBars',0,int(height/2),myRadTrackBar)
cv2.createTrackbar('myMoveWinX', 'myTrackBars',0,1080,myMoveWinXTrackBar)
cv2.createTrackbar('myMoveWinY', 'myTrackBars',0,620,myMoveWinYTrackBar)
cv2.createTrackbar('WinSize', 'myTrackBars',width,1080,myNewWinSize)
while True:
    ignore, frame = cam.read()
    cv2.circle(frame,(xPos,yPos),myRadius,(0,0,255),2)
    cv2.imshow('myWin',frame)
    #cv2.moveWindow('myWin',0,0)
    #cv2.resizeWindow('myWin',newWidth,newHeight)
    cv2.moveWindow('myWin',myMoveWinX,myMoveWinY)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release