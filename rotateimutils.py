def rotate(image,angle,centre=None,scale=1.0):
    (h,w) = image.shape[:2]
    if centre is None:
        centre = (w//2,h//2)
    M = cv2.getRotationMatrix2D(centre,angle,scale)
    rotated = cv2.wrapAffine(image,M,(w,h))
    return rotated

rotated = imutils.rotate(image,180)
cv2.imshow("Rotated by 180 Degree",rotated)
cv2.waitKey
