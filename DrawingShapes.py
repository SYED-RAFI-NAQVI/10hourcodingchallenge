import numpy as np
import cv2 as cv


img = cv.imread('1.jpeg',cv.IMREAD_COLOR)
#rectangel have 4 arguments.... Image dir, start point, end point, color of line, width of line.
cv.rectangle(img, (180,0), (280,120), (0,255,0), 9)

#here we use redius insted of endpoint.
#here color is not rgb but bgr so first 0 is blue 210 is green and 200 is red and if we use width -1
#then it will fill in total given color.
cv.circle(img, (40,50), 20, (0,210,200), -1)


#here image is the name and img is object to work on...
cv.imshow('image', img)

#waitKey helps to wait for any key
cv.waitKey(0)

#finally destroy all windows
cv.destroyAllWindows()