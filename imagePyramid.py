import cv2 
import numpy as np 
img = cv2.imread("sky.jpg")
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
cv2.imshow("Original Image",img)
print(lr1.shape)
print(img.shape)
print(lr2.shape)
# print(img.shape)
cv2.imshow("ResolutionDOwnlr2 Image",lr2)
cv2.waitKey(0)
cv2.destroyAllWindows()