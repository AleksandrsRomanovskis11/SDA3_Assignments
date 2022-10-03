import cv2

image = cv2.imread('Assignment0/strumpe.jpg',1)

rotated_image = cv2.imread('Assginment0/strumpe.jpg',1)
height,width = image.shape[:2]  #dividing height and width by 2 to get the center of the image


center = (width/2, height/2) # get the center coordinates of the image to create the 2D rotation matrix

rotate_matrix = cv2.getRotationMatrix2D(center = center, angle=45,scale=1) 

rotated_image = cv2.warpAffine(src =image, M=rotate_matrix, dsize=(width,height))

#rotated_image = cv2.imread('rotated_image',1)
cv2.imshow ('Original_image',image)
cv2.imshow ('Rotated_image',rotated_image)
cv2.waitKey(0)
