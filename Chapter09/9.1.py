import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
        _, image = cap.read()
        cv2.imshow("Frame", image)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


        lowerGreen = np.array([80,50,50])
        upperGreen = np.array([130,255,255])

        mask = cv2.inRange(hsv, lowerGreen, upperGreen)
        res = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow('mask',mask)
        cv2.imshow('result',res)
        key = cv2.waitKey(1) & 0xFF


        if key == ord('q'):
                break
cv2.destroyAllWindows()
cap.release()