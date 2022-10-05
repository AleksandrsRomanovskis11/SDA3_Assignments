import cv2

import numpy as np 

image = cv2.imread('Assignment0/strumpe.jpg',0)

kernel1 = np.array([[0, -1,  0],

                   [-1,  5, -1],

                    [0, -1,  0]])


image_blurred = cv2.filter2D(src=image, ddepth=1, kernel=kernel1)

cv2.imshow('Original',image)
cv2.imshow('blurred',image_blurred)

cv2.waitKey(0)

cv2.destroyAllWindows()

