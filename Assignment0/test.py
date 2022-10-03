import cv2

image_greyscale = cv2.imread("Assignment0/strumpe.jpg",1)
#cv2.imshow("image grayscale", image_greyscale)


# let's downscale the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_height, down_width)
resized_down = cv2.resize(image_greyscale, down_points, interpolation= cv2.INTER_LINEAR)

# let's upscale the image using new  width and height

up_width = 600
up_height = 400
up_points = (up_width, up_height) 
resized_up = cv2.resize(image_greyscale, up_points, interpolation=cv2.INTER_LINEAR)


cv2.imshow('Resized down by defining height and width',resized_down)
cv2.waitKey()
cv2.imshow('Resized up by defining height and width',resized_up)
cv2.waitKey()

cv2.destroyAllWindows()



