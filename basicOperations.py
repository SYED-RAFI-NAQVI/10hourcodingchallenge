import numpy as np
import cv2 as cv

img = cv.imread('1.jpeg',1)

#can check the image paticular pixel color 
px = img[55,55]

#[55,55] pixel color
print(px)

#can change the pixel color or maniplate the pixel color
img[55,55] = [255,255,255]

#again checking pixel color
print(px)


#####   RANGE OF IMAGE #####

#actully asking the pixel values of 100 to 150 region but we use 96x96,1024x1024 to indicate the size so here we use two values as 100:150
roi = img[100:150,100:150]

print(roi)

#we can change the color of any pixel as well as any region of image (red color)
img[100:150,100:150] = [0,0,255]

#we can redfine a new image of same image on same image
body = img[30:120,100:200]
img[0:90,0:100] =body


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()