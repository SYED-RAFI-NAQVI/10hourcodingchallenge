import numpy as np
import cv2  as cv

img1 = cv.imread('2.png')
img2 = cv.imread('3.png')

add = img1 + img2

#this is another method which adds all the pixel values by that image produce somuch of white color so by that we cant even see the image.
#######         add = cv.add(img1,img2)         #########

# addWighted helps to add two images by its wights with its ratios, 1.image to add , 2.wight, 3.image to add, 4.wight of secound image, 5.alpha channel.
weight = cv.addWeighted(img1, 0.4, img2, 0.6, 0)
 

cv.imshow('add',add)
cv.imshow('weight', weight)
cv.waitKey(0)
cv.destroyAllWindows()