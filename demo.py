# IMAGE READ AND DISPLAY


# 1.Image pixel find
# import   cv2
# image=cv2.imread('fruit.jpg',1)
# print(image)

# import cv2
# image=cv2.imread('fruit.jpg',1)
# cv2.imshow('image',image)
# cv2.waitKey(10000)
# cv2.imwrite('fruit.png',image)
# cv2.destroyAllWindows()


# shapes
# 1.line
# import cv2
# image=cv2.imread('fruit.jpg',1)
# cv2.line(image,(0,0),(600,600),(255,0,0),5)
# cv2.imshow('shapes',image)
# cv2.waitKey(0)

# 2.rectangle
# import cv2
# image=cv2.imread('fruit.jpg',1)
# cv2.rectangle(image,(0,0),(400,400),(0,255,255),5)
# cv2.imshow('shapes',image)
# cv2.waitKey(0)

# # 3.circle
# import cv2
# image=cv2.imread('fruit.jpg',1)
# cv2.circle(image,(400,400),100,(0,0,255),-1)
# cv2.imshow('shapes',image)
# cv2.waitKey(0)

# text varunnathinu
import cv2
image=cv2.imread('fruit.jpg',1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'hello',(100,100),font,4,(255,0,0),cv2.LINE_AA)
cv2.imshow('shapes',image)
cv2.waitKey(0)



# import cv2
# image=cv2.imread('fruit.jpg',1)
# cv2.line(image,(0,0),(600,600),(0,255,0),4)
# cv2.rectangle(image,(0,0),(600,600),(0,0,255),5)
# cv2.circle(image,(300,300),100,(255,0,255),-1)
# font=cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(image,"karthika",(60,100),font,4,(255,0,255),cv2.LINE_AA)
# cv2.imshow('shapes',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
