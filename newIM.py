import numpy as np
import cv2 as cv

img = cv.imread('1.jpeg', cv.IMREAD_COLOR)
cv.line(img, (0,34), (44,65), (255,255,255), 8)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()