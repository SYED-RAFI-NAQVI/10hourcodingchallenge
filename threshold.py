import numpy as np 
import cv2 as cv 

img = cv.imread('4.jpg')
ret, thresh = cv.threshold(img, 12, 255, cv.THRESH_BINARY)
print(ret)

#this helps to convert the color image to the gray image...
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret2, thresh2 = cv.threshold(gray, 12, 255, cv.THRESH_BINARY)
gaus = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)


cv.imshow('img',img)
cv.imshow('thresh',thresh)
cv.imshow('gray',gray)
cv.imshow('thresh2',thresh2)
cv.imshow('gaus',gaus)
cv.imwrite('./finalImg.jpg',gaus)
cv.waitKey(0)
cv.destroyAllWindows()