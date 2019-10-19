
import cv2
import numpy as np
import time
import threading
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame = cap.read()
else:
        ret = False
while ret:

        ret,frame = cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # Green Color
        Glow = np.array([20,70,70])
        Ghigh = np.array([80,255,255])

        # Blue Color
        Blow = np.array([100,50,50])
        Bhigh = np.array([140,255,255])

        # Red Color
        Rlow = np.array([140,150,0])
        Rhigh = np.array([180,255,255])

        GImage_mask = cv2.inRange(hsv,Glow,Ghigh)
        BImage_mask = cv2.inRange(hsv,Blow,Bhigh)
        RImage_mask = cv2.inRange(hsv,Rlow,Rhigh)

        green = cv2.bitwise_and(frame,frame,mask= GImage_mask)
        blue = cv2.bitwise_and(frame,frame,mask=BImage_mask)
        red = cv2.bitwise_and(frame,frame,mask=RImage_mask)

        Gcontours,c2 = cv2.findContours(GImage_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        Rcontours,c2 = cv2.findContours(RImage_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        Bcontours,c2 = cv2.findContours(BImage_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        if Gcontours:
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)

        if Bcontours:
            GPIO.output(14, GPIO.HIGH)
        else:
            GPIO.output(14, GPIO.LOW)

        if Rcontours:
            GPIO.output(15, GPIO.HIGH)
        else:
            GPIO.output(15, GPIO.LOW)

        cv2.drawContours(frame,Gcontours,-1,(0,255,0),3)
        cv2.drawContours(frame,Rcontours,-1,(0,0,255),3)
        cv2.drawContours(frame,Bcontours,-1,(255,0,0),3)

        cv2.imshow("Original",frame)
        cv2.imshow("Green Image Mask",green)
        cv2.imshow("Blue Image Mask",blue)
        cv2.imshow("Red Image Mask",red)
        
        GPIO.output(18, GPIO.LOW)
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

        if cv2.waitKey(1)==27:
            break
cv2.destroyAllWindows()
cap.release()