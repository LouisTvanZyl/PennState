import cv2
img = cv2.imread('Image_Recognition\overwatch.jpg',1)

print(img)

img = cv2.line(img,(0,0), (255,255),(255,60,200),5)

cv2.imshow("image",img)
cv2.waitKey(5000)

cv2.destroyAllWindows()