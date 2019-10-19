import cv2
import time
#import RPi.GPIO as GPIO
import  numpy as np

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO.setup(14,GPIO.OUT)

def nothng(x):
    pass
face_cascade = cv2.CascadeClassifier("Image_Recognition\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Image_Recognition\haarcascade_eye_tree_eyeglasses.xml")
cap = cv2.VideoCapture(0)

#cv2.namedWindow("Tracking")
#cv2.createTrackbar("LH","Tracking",0,255,nothng)
#cv2.createTrackbar("LS","Tracking",0,255,nothng)
#cv2.createTrackbar("LV","Tracking",0,255,nothng)
#cv2.createTrackbar("UH","Tracking",255,255,nothng)
#cv2.createTrackbar("US","Tracking",255,255,nothng)
#cv2.createTrackbar("UV","Tracking",255,255,nothng)

while True:
    #frame = cv2.imread("Image_Recognition\overwatch.jpg")
    time.sleep(0)
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    faces = face_cascade.detectMultiScale(frame, 1.1 ,4)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for(x,y,w,h)in faces:
        if(x>0 or x!=None):
            #GPIO.output(14,GPIO.HIGH)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)
            print("Face dimetntions X-axis {0} Y-Axis {1} Height {2} Width {3}".format(x,y,h,w))
            roi_grey = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_color)
            
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                print("Eye dimetntions X-axis {0} Y-Axis {1} Height {2} Width {3}".format(ex,ey,eh,ew))
        else:
            #GPIO.output(14,GPIO.LOW)
            print("no face")

    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_s = cv2.getTrackbarPos("LS","Tracking")
    l_v = cv2.getTrackbarPos("LV","Tracking")

    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow("Frame",frame)
    #cv2.imshow("mask",mask)
    #cv2.imshow("res",res)

    key = cv2.waitKey(1)

    if key ==  27:
        break
cap.release()
cv2.destroyAllWindows()