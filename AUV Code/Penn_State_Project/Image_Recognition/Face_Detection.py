import cv2
face_cascade = cv2.CascadeClassifier("Image_Recognition\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey,1.1,4)

    for(x,y,w,h )in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)
    cv2.imshow("frame",frame)
    cv2.waitKey()
    
    if cv2.waitKey(1):
        break

cap.release()