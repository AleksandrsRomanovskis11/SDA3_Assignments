import cv2
from cv2 import LINE_AA

image = cv2.imread('Assignment0/strumpe.jpg',1)

cv2.imshow('Annotation',image)

if image is None:
    print('Could not read image')

imageLine = image.copy()

#Draw the image from point A to B

pointA = (200,80)
pointB = (450,80)

cv2.line (imageLine, pointA, pointB, (255,255,0), thickness=3, lineType=cv2.LINE_AA )
cv2.imshow ('Imagine Line' ,imageLine)






cv2.waitKey(0)

