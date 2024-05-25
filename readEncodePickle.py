import os
import cv2
import face_recognition as fr
import pickle
with open('encodedPickle.pkl','rb') as f:
    masterEncodes = pickle.load(f)
    masterNames = pickle.load(f)
    for name, picEncode in zip(masterNames,masterEncodes):
        cv2.imshow(name,picEncode)
        cv2.waitKey(2500)
        cv2.destroyWindow(name)