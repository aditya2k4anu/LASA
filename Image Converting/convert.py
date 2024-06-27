import cv2

image = cv2.imread('C:\\Users\\adity\\OneDrive\\Desktop\\Image Converting\\rose.jpg',cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh, img_black = cv2.threshold(gray,170,250,cv2.THRESH_BINARY)

cv2.imshow('rose.jpg',img_black)

#cv2.imwrite('rose_gray.png',gray)

cv2.imwrite('rose_black.png',img_black)

cv2.waitKey(0)
cv2.destroyAllWindows()
