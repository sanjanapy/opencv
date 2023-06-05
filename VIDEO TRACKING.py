import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('image',new_image)
    lowerbound=np.array([110,50,50])
    upperbound=np.array([130,256,256])
    mask=cv2.inRange(new_image,lowerbound,upperbound)
    cv2.imshow('mask',mask)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(0)
    if k == 27:
        break
cv2.destroyAllWindows()