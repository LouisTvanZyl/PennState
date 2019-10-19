import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame = cap.read()
else:
        ret = False
while ret:

        ret,frame = cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        Blow = np.array([100,50,50])
        Bhigh = np.array([140,255,255])

        BImage_mask = cv2.inRange(hsv,Blow,Bhigh)

        contours, hierarchy =cv2.findContours(BImage_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        for contour in contours:
         cv2.drawContours(frame , contour , -1 , (25,100,5), 3)

        print(contours)

        cv2.imshow("Frame",frame)
        cv2.imshow("Mask",BImage_mask)

        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()