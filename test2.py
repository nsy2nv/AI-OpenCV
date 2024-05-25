import cv2
import face_recognition as fr
font = cv2.FONT_HERSHEY_SIMPLEX

donFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/demoImages/known/Donald Trump.jpg')
faceLoc = fr.face_locations(donFace)[0]
donFaceEncode = fr.face_encodings(donFace)[0]

nancyFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/demoImages/known/Nancy Pelosi.jpg')
faceLoc = fr.face_locations(nancyFace)[0]
nancyFaceEncode = fr.face_encodings(nancyFace)[0]

penceFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/demoImages/known/Mike Pence.jpg')
faceLoc = fr.face_locations(penceFace)[0]
penceFaceEncode = fr.face_encodings(penceFace)[0]

knownEncodings = [donFaceEncode, nancyFaceEncode,penceFaceEncode]
names = ['Donald Trump','Nancy Pelosi', 'Mike Pence']

unknownFace = fr.load_image_file('C:/Users/MTN-SIMREG/OneDrive/Desktop/Open_Doors/OpenCv/demoImages/unknown/u1.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations = fr.face_locations(unknownFace)
unknownEncodings = fr.face_encodings(unknownFace,faceLocations)

for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
    top, right, bottom, left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(0,255,0),2)
    name = 'unknown person'
    matches = fr.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex = matches.index(True)
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,.60,(255,0,0),2)

cv2.imshow('myWin', unknownFaceBGR)
cv2.waitKey(1000000) 
    