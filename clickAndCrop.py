import cv2
evt = 0
def clickCrop(event, xPos, yPos, flags, params):
    global evt
    global start_pnt 
    global end_pnts
    if event == cv2.EVENT_LBUTTONDOWN:
        evt = event
        start_pnt = (xPos,yPos)
        print('start Point',start_pnt)
    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        end_pnts = (xPos,yPos)
        print('End point',end_pnts)
    if event == cv2.EVENT_RBUTTONUP:
        evt = event
width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))
cv2.namedWindow('Win1')
cv2.setMouseCallback('Win1',clickCrop)
while True:
    ignore, frame = cam.read()
    if evt == 4:
        if end_pnts[1]>start_pnt[1]:
            cv2.rectangle(frame,start_pnt,end_pnts,(0,0,255),2)
            frameROI = cv2.rectangle(frame[start_pnt[1]:end_pnts[1],start_pnt[0]:end_pnts[0]],start_pnt,end_pnts,(0,0,255),2)
            cv2.imshow('ROI', frameROI)
            cv2.moveWindow('ROI',width,0)
        else:#Check if the user is cropping from down upward
            temp = start_pnt
            start_pnt = end_pnts
            end_pnts = temp
            frameROI = cv2.rectangle(frame[start_pnt[1]:end_pnts[1],start_pnt[0]:end_pnts[0]],start_pnt,end_pnts,(255,0,0),2)
            cv2.imshow('ROI', frameROI)
            cv2.moveWindow('ROI',width,0)
    if evt == 5:
        cv2.destroyWindow('ROI')
        evt = 0
    cv2.imshow('Win1', frame)
    cv2.moveWindow('Win1', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release