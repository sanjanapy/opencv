# import cv2
# import numpy as np
# image=cv2.imread('blur.jpg',1)
# blur=cv2.blur(image,(5,5))
# gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
# cv2.imshow('image',image)
# cv2.imshow('blur',blur)
# cv2.imshow('gaussian_blur',gaussian_blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
import cv2
import numpy as np
image = cv2.imread('blur.jpg',0)
blur=cv2.blur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('blur',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()