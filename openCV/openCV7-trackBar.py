import cv2

print(cv2.__version__)

def nothing():
    pass

cam = cv2.VideoCapture(0)
cv2.namedWindow('picam')
cv2.createTrackbar('xVal','picam',0,500,nothing)
cv2.createTrackbar('yVal','picam',0,500,nothing)

while True:
    ret, frame = cam.read()

    xVal =cv2.getTrackbarPos('xVal','picam')
    yVal =cv2.getTrackbarPos('yVal','picam')
    
    cv2.circle(frame,(xVal,yVal),5,(255,0,0), -1)

    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)

    if cv2.waitKey(1) == ord ('q'):
        break

cam.release()
cv2.destroyAllWindows()
