import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)

def make_1080p():
   cap.set(3,1920) # set Width
   cap.set(4,1080) # set Height   

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20, 20))
    for (x,y,w,h) in faces:    
        print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),4)    

    cv2.imshow('img',img)
    k = cv2.waitKey(0) & 0xff
    if k == 13: # press 'ENTER' to quit
        break

cap.release()
cv2.destroyAllWindows()
