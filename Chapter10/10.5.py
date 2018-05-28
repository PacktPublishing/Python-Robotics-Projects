import numpy as np
import cv2
Import RPi.GPIO as GPIO

Motor1F = 20
Motor1R = 21
Motor2F = 2
Motor2R = 3
Buzzer = 24

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
GPIO.setup(Motor1a,GPIO.OUT)
GPIO.setup(Motor1b,GPIO.OUT)
GPIO.setup(Motor2a,GPIO.OUT)
GPIO.setup(Motor2b,GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

def forward():

        GPIO.output(Motor1F,1)
        GPIO.output(Motor1R,0)
        GPIO.output(Motor2F,1)
        GPIO.output(Motor2R,0)

def backward():

        GPIO.output(Motor1F,0)
        GPIO.output(Motor1R,1)
        GPIO.output(Motor2F,0)
        GPIO.output(Motor2R,1)

def stop():

        GPIO.output(Motor1F,0)
        GPIO.output(Motor1R,0)
        GPIO.output(Motor2F,0)
        GPIO.output(Motor2R,0)

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainningData.yml")

id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

 ret, img = cam.read()
 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces = faceDetect.detectMultiScale(gray,1.3,5)

 for (x,y,w,h) in faces:
     cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
     id, conf = rec.predict(gray[y:y+h, x:x+w])

     if id==1:
         id = "BEN"

         forward()
         time.sleep(1)
         stop()
         time.sleep(5)
         backward()
         time.sleep(1)

     else :

         GPIO.output(Buzzer, 1)
         time.sleep(5)

     cv2.putText(img, str(id), (x,y+h),font,2, (255,0,0),1,cv2.LINE_AA)
     cv2.imshow("face", img)

 id = 0 
 if cv2.waitKey(1)==ord('q'):
 break

cam.release()
cv2.destroyAllWindows()