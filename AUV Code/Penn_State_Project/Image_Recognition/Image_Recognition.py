import cv2

#Image Reading
img = cv2.imread('Image_Recognition\overwatch.jpg',0)

print(img)
#tested
cv2.imshow("image",img)
cv2.waitKey(5000)

cv2.destroyAllWindows()

#Play via File

#vidcap = cv2.VideoCapture('Image_Recognition\test.mp4')

#while(vidcap.isOpened()):
    #ret, frame = vidcap.read()
    #cv2.imshow('frame',frame)

#Using a camera
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    
    ret, frame = cap.read()
    
    cv2.imshow("frame",frame)
    
cap.release()