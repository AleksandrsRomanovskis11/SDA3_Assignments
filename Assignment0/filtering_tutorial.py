import cv2

import numpy as np 

image = cv2.imread('Assignment0/strumpe.jpg',0)

image_blurred = cv2.blur(src=image, ksize=(5,5))



cv2.imshow('Original',image)
cv2.imshow('blurred',image_blurred)

cv2.waitKey(0)

cv2.destroyAllWindows()

