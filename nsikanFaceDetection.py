import cv2
import face_recognition as fr
width = 640
height = 360
font = cv2.FONT_ITALIC
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc(*'MJPG'))

nsikanFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/myFamilyImages/Nsikan.jpg')
faceLoc = fr.face_locations(nsikanFace)[0]
nsikanEncode = fr.face_encodings(nsikanFace)[0]

lovethFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/myFamilyImages/Loveth.jpg')
faceLoc = fr.face_locations(lovethFace)[0]
lovethEncode = fr.face_encodings(lovethFace)[0]

divineFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/myFamilyImages/Divine.jpg')
faceLoc = fr.face_locations(divineFace)[0]
divineEncode = fr.face_encodings(divineFace)[0]

emediongFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/myFamilyImages/Emediong.jpg')
faceLoc = fr.face_locations(emediongFace)[0]
emediongEncode = fr.face_encodings(emediongFace)[0]

abrahamFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/myFamilyImages/Abraham.jpg')
faceLoc = fr.face_locations(abrahamFace)[0]
abrahamEncode = fr.face_encodings(abrahamFace)[0]

knownEncodings = [nsikanEncode,lovethEncode,divineEncode,emediongEncode,abrahamEncode]
names = ['Nsikan','Loveth','Divine','Emediong','Abraham']
faceCascade = cv2.CascadeClassifier('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/PythonAI/haar/haarcascade_frontalface_default.xml')
while True:
    ignore, frame = cam.read()
    faces = faceCascade.detectMultiScale(frame,1.3,5)
    for face in faces:
        xpos,ypos,width,height = face
        faceLocations = fr.face_locations(cv2.rectangle(frame,(xpos,ypos),(xpos+width,ypos+height),(0,255,0),2))
        unknownEncodings = fr.face_encodings(frame,faceLocations)
        
        for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
            name = 'unknown person'
            matches = fr.compare_faces(knownEncodings,unknownEncoding)
            if True in matches:
                matchIndex = matches.index(True)
                name = names[matchIndex]
            cv2.putText(frame,name,(xpos,ypos),font,.6,(255,0,0),2)
    cv2.imshow('win',frame)
    cv2.moveWindow('win',0,0)  
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows
