import cv2
width = 1280
height = 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))
rows = int(input('How many rows would you like? '))
columns = int(input('How many columns do you like? '))
while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(int(width/columns),int(height/columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            windName = 'View '+ str(i)+' X '+str(j)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName,int((width/columns)*j), int((height/columns+30)*i))
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()