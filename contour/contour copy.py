import cv2
import numpy as np
import pytesseract

img = cv2.imread("C:\\TEMP\\20240522\\05.jpg")
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
flt = cv2.adaptiveThreshold(gry,
                            100, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 13, 16)


krn = np.ones((3, 3), np.uint8)
opn = cv2.morphologyEx(flt, cv2.MORPH_OPEN, krn)

cv2.imshow('img', opn)
cv2.waitKey(0)   
cls = cv2.morphologyEx(opn, cv2.MORPH_CLOSE, krn)

cv2.imshow('img', cls)
cv2.waitKey(0)   
gry = cv2.bitwise_or(gry, cls)


cv2.imshow('img', gry)
cv2.waitKey(0)   
txt = pytesseract.image_to_string(gry)
print(txt[2:])
