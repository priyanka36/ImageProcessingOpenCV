import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('sky.png',0)
histg = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histg)
plt.show()