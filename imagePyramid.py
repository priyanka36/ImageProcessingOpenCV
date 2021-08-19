import cv2 
import numpy as np 
img = cv2.imread("sky.jpg")
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# cv2.imshow("Original Image",img)
# print(lr1.shape)
# print(img.shape)
# print(lr2.shape)
# print(img.shape)
layer = img.copy()
grp = [layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    grp.append(layer)
    # cv2.imshow(str(i),layer)

layer = grp[5]
cv2.imshow("ULGP",layer)
lp = [layer]

for i in range(5,0,-1):
    guassian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp(i-1),guassian_extended)
    cv2.imshow(str(i),laplacian)

# cv2.imshow("ResolutionDOwnlr2 Image",lr2)
cv2.waitKey(0)
cv2.destroyAllWindows()