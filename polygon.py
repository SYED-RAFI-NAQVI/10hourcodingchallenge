import numpy as np
import cv2 as cv

img = cv.imread('1.jpeg',cv.IMREAD_COLOR)

#for polygon we need to have set of points so we create a numpy array. and pts is an object.

pts = np.array([[20,33],[300,120], [67,79], [123,111], [144,134]], np.int32)

#the method polylines will actully draws a polygon by taking different parametes, 1.where to draw (img),
#2.which set of points, 3.checks first and last point should be connected or not by (bool), 4.color, 5.widht of line.
cv.polylines(img, [pts], True,(0,231,123), 1)



cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()