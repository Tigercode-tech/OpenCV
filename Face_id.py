import cv2
img = cv2.imread('C:/Users/ridha/Jetlearn/Images/faces.jpg')
program = cv2.CascadeClassifier('C:/Users/ridha/Jetlearn/OpenCV/haarcascade_frontalface_default.xml')
faces = program.detectMultiScale(img)
print(faces)
for i in faces:
    cv2.rectangle(img, (i[0] , i[1]), (i[0]+i[2], i[1]+i[3]), (255, 255, 0), (2))
cv2.imshow("image of faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

