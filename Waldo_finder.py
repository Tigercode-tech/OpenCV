import cv2
import numpy as np

fullpicture = cv2.imread("C:/Users/ridha/Jetlearn/Images/Where.jpg")
waldo = cv2.imread(r"C:\Users\ridha\Jetlearn\Images\Waldo.png")

method = cv2.TM_CCOEFF
findit = cv2.matchTemplate(fullpicture, waldo, method)

min, max, coomi, cooma = cv2.minMaxLoc(findit)

x, p = cooma
he, wi, coch = waldo.shape

donei = cv2.rectangle(fullpicture, cooma, (x+wi, p+he), (0, 0, 255), 25)

start = cooma
end = (x+wi, p+he)
vert = slice(p, p+he)
horz = slice(x, x+wi)

hr = (fullpicture[vert, horz])
zeroes = np.zeros(fullpicture.shape, dtype='uint8')
import cv2
import numpy as np

fullpicture = cv2.imread("C:/Users/ridha/Jetlearn/Images/Where.jpg")
waldo = cv2.imread(r"C:\Users\ridha\Jetlearn\Images\Waldo.png")

method = cv2.TM_CCOEFF
findit = cv2.matchTemplate(fullpicture, waldo, method)

min, max, coomi, cooma = cv2.minMaxLoc(findit)

x, p = cooma
he, wi, coch = waldo.shape

donei = cv2.rectangle(fullpicture, cooma, (x+wi, p+he), (0, 0, 255), 3)

start = cooma
end = (x+wi, p+he)
vert = slice(p, p+he)
horz = slice(x, x+wi)

hr = (fullpicture[vert, horz])
zeroes = np.zeros(fullpicture.shape, dtype='uint8')
disp = cv2.addWeighted(fullpicture, 0.3, zeroes, 0.8 ,0)
disp[p:p+he, x:x+wi]  = waldo

cv2.imshow("window name", disp)
cv2.waitKey(0)
cv2.destroyAllWindows()
