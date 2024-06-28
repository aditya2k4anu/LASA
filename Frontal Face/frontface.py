import cv2

front_face = cv2.CascadeClassifier('haarcascadeshaarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    print(img)
    c = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    d = front_face.detectMultiScale(c,1.5,5)

    for (x,y,w,h) in d:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
