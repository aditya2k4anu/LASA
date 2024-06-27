import cv2
face = cv2.CascadeClassifier('datahaarcascadeshaarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    print(ret)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = face.detectMultiScale(g,1.3,5)
    
    for (x,y,w,h) in f:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 5)
        
    cv2.imshow('img', img)
    k=cv2.waitKey(30) & 0xff

    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
