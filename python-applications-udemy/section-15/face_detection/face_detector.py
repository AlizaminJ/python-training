import cv2

# reszing the image
img = cv2.imread("photo_CV.jpg",1)
resized_image=cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/1.5)))
cv2.imshow("AlizaminJ", resized_image)
cv2.waitKey(3000)
cv2.destroyAllWindows()
cv2.imwrite("AlizaminJ.jpg", resized_image)


# FACE DETECTION
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("news.jpg") # try first AlizaminJ

# openCV works better on gray images
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, #important to start at a new line
scaleFactor=1.05,
minNeighbors=5)

for x, y, w, h in faces:
    rect_img=cv2.rectangle(img, (x,y), (x+w, y+h), (0, 250, 0),3) # (0, 250, 0) stands for color while 3 is the width

print(type(faces))
print(faces)

cv2.imshow("Gray", rect_img)
cv2.waitKey(0)
cv2.destroyAllWindowsWindow()

