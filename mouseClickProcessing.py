import cv2
evt = 0
def mouseClick(event,xPos,yPos,flags,params):
    global evt 
    global pnt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('The mouse event was ',event)
        print('at the position ', xPos, yPos)
        evt = event
        pnt = (xPos,yPos)
    if event == cv2.EVENT_LBUTTONUP:
        print('The mouse event was ', event)
        print('at the position ', xPos, yPos)
        evt = event
    if event == cv2.EVENT_RBUTTONUP:
        print('Right Button up ',event)
        evt = event
        pnt = (xPos,yPos)
    
width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cv2.namedWindow('my webcam')
cv2.setMouseCallback('my webcam', mouseClick)
while True:
    ignore, frame = cam.read()
    if evt == 1 or evt == 4:
        cv2.circle(frame,pnt,25,(255,0,0),2)
    cv2.imshow('my webcam', frame)
    cv2.moveWindow('my webcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release
