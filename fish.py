import cv2

# path
path = r'D:\hello\books\python\SUPDetection\test_img.jpg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (0, 0)
# represents the top left corner of image
print(image.shape)
x,y = image.shape[0],image.shape[1]
print(x)
print(y)
start_point = (1000,0)

# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (1000,y)

# Green color in BGR
color = (0, 255, 0)

# Line thickness of 9 px
thickness = 9

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

