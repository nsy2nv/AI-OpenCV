import os
import cv2
import face_recognition as fr
import pickle
imageDirs = 'C:\\Users\\MTN-SIMREG\\OneDrive\\Desktop\\Open_Doors\\OpenCv\\demoImages\\known'
for root, folder, files in os.walk(imageDirs):
    #print('Working path: ',root)
    #print('Folders in the path:',folder)
    #print('Files in my folder: ',files)
    masterEncodes = []
    masterNames = []
    for file in files:
        fullFilePath  = os.path.join(root,file)
        facesArray = fr.load_image_file(fullFilePath)
        facesArray = cv2.cvtColor(facesArray,cv2.COLOR_RGB2BGR)
        faceLoc = fr.face_locations(facesArray)[0]
        faceEncode = fr.face_encodings(facesArray)[0]
        name = os.path.splitext(file)[0]
        masterEncodes.append(faceEncode)
        masterNames.append(name)
    with open('encodedPickle.pkl', 'wb') as f:
        pickle.dump(masterEncodes, f)
        pickle.dump(masterNames, f)
        #cv2.imshow(file,facesArray)
        #cv2.waitKey(2500)
        #cv2.destroyWindow(file)
    #print('Master Encoding ',masterEncodes)
    #print('Names ',masterNames)
       
