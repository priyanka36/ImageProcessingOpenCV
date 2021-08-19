import cv2 
import numpy as np 
apple = cv2.imread("Apple.jpg")
orange = cv2.imread("Orange.jpg")

print(apple.shape)
print(orange.shape)

cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.waitKey(0)