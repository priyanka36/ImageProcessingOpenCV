import cv2 
import numpy as np 

img = cv2.imread("sky.jpg",0)
img= cv2.resize(img,(500,500))

# _,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
#If the value of the pixel is less than 200 then it is assigned as black and if the value of the pixel
#above 200 is assigned white
# _,th2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
#upto threshold the pixel values will not change after certain threshold the values
#the pixel values will be the same for example after 200 all pixel values will be assigned to 200
_,th4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)

#All the pixel values less than threshold will be asssigned to zero


cv2.imshow("Image",img)
# cv2.imshow("TH1",th1)
# cv2.imshow("TH2",th2)
cv2.imshow("TH5",th4)
# cv2.imshow("th1",th1)
cv2.waitKey(0)
