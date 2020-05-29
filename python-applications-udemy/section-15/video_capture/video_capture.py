import cv2, time 

video=cv2.VideoCapture(0) # video cams will be indexed depending on number of cams, here zero stands for frontweb cam  or just path to the file

a = 0
while True:
    a = a + 1 # niee trick to know number of iterations
    check, frame = video.read()

    print(check)
    print(frame)

    #time.sleep(5)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Recording", frame) # frame or gray
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows
