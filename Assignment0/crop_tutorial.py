import cv2
import numpy as np

image = cv2.imread ('Assignment0/strumpe.jpg',1)

print(image.shape) # prints shape of the image/size of the image in pixels

#cv2.imshow("crop", image) # showing just picture , not cropped one

#cropped_image= image [100:1000, 900:1500]

cropped_image = cv2.imread ('Assignment0/strumpe.jpg',1)
cropped_image= image [100:1000, 900:1500]

cv2.imshow ("cropped", cropped_image)

cv2.imwrite('cropped_image.jpg', cropped_image)





cv2.waitKey(0)
cv2.destroyAllWindows()

