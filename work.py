
# # object tracking
# import cv2
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(image,(x,y),100,(0,255,0),-1)
# image=cv2.imread('fruit.jpg',1)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#     cv2.imshow('image',image)
#     if cv2.waitKey(20)& 0xFF ==27:
#         break
#
# cv2.destroyAllWindows()

import cv2
image=cv2.imread('gradient 1.jpg',0)
ret,thresh=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('image',image)
cv2.imshow('thres',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
