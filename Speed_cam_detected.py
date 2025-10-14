import cv2

vid = cv2.VideoCapture(r'C:\Users\ridha\Jetlearn\Images\cars.mp4')
detector = cv2.CascadeClassifier(r'C:\Users\ridha\Jetlearn\OpenCV\haarcascade_license_plate_rus_16stages.xml')

while True:
    value, pixels = vid.read()
    cv2.cvtColor(pixels, cv2.COLOR_BGR2GRAY)
    video = detector.detectMultiScale(pixels, 1.4)
    for q in video:
        cv2.rectangle(pixels, (q[0] , q[1]), (q[0]+q[2], q[1]+q[3]), (0, 255, 255), (2))
    cv2.imshow('detector', pixels)
    if cv2.waitKey(1) == 32:
        break