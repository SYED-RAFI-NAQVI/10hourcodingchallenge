import numpy as np
import cv2 as cv

img = cv.imread('1.jpeg',cv.IMREAD_COLOR)

#we have opencv fonts so TRIPLEX is one of the fonts of opencv
font = cv.FONT_HERSHEY_TRIPLEX

#can add text by putText function or method where parameters are 1. where to write(image), 2.text , 3.starting point, 4.which type of font,
#5.size of font, 6.color of font, 7.thickness of font, 8.recommanded by openCV to have LINE_AA when adding a text on image.
cv.putText(img, 'I can write here', (0,120), font, 1,(20,21,253), 3, cv.LINE_AA)


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()