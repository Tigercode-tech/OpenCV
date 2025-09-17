import cv2
video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('C:/Users/ridha/Jetlearn/OpenCV/haarcascade_frontalface_default.xml')
while True: 
    val, pix = video.read()
    vid = cascade.detectMultiScale(pix)
    for i in vid:
        cv2.rectangle(pix, (i[0] , i[1]), (i[0]+i[2], i[1]+i[3]), (0, 255, 255), (2))
    cv2.imshow('video', pix)
    if cv2.waitKey(1) == 32:
        break
    