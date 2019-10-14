#Simple Face Detection code

import cv2

def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

test = cv2.imread('test.jpg')

gray_img = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
print('Number of Faces found: ', len(faces))

for (x, y, w, h) in faces:
 cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found", test)
cv2.waitKey(0)