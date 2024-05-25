import cv2
width = 360
height = 180
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*'MJPG'))


while True:
    ignore, frame = cam.read()
    cv2.imshow('webcam1',frame)
    cv2.moveWindow('webcam1', 0, 0)

    cv2.imshow('webcam2',frame)
    cv2.moveWindow('webcam2', 360, 0)

    cv2.imshow('webcam3',frame)
    cv2.moveWindow('webcam3', 720, 0)

    cv2.imshow('webcam4',frame)
    cv2.moveWindow('webcam4', 1080, 0)

    cv2.imshow('webcam5',frame)
    cv2.moveWindow('webcam5', 0, 260)

    cv2.imshow('webcam6',frame)
    cv2.moveWindow('webcam6', 360, 260)

    cv2.imshow('webcam7',frame)
    cv2.moveWindow('webcam7', 720, 260)

    cv2.imshow('webcam8',frame)
    cv2.moveWindow('webcam8', 1080, 260)



    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()