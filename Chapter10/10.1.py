import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:

        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
       
        for (x,y,w,h) in faces:
           cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow('img',img)

        k = cv2.waitKey(1) & 0xff
        if k == ord(‘q’):
                break

cap.release()
cv2.destroyAllWindows()