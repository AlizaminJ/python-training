# pip install opencv-python

import cv2

# grye image
img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img.shape)
print(img)
print(img.ndim) # to check dimensions

#color image
img1 = cv2.imread("galaxy.jpg",1)
print(type(img1))
print(img1.shape)
print(img1)
print(img1.ndim)

cv2.imshow("galaxy", img)
cv2.waitKey(2000)  # 2 seconds try 0 -> user will close
cv2.destroyAllWindows()

# to resize the pic
resized_image=cv2.resize(img,(1000,500))
cv2.imshow("galaxy", resized_image)
cv2.waitKey(0)  # 0 -> user will close
cv2.destroyAllWindows()

# reducing size by 2
resized_image2=cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
cv2.imshow("galaxy", resized_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("galaxy_resized.jpg", resized_image2)

