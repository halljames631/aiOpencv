import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    roi = frame[50:250,200:400].copy()

    roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)

    frame[50:250,200:400] = roiGray

    cv2.imshow('ROI',roi)
    cv2.imshow('picam', frame)
    cv2.imshow('gray',roiGray)

    cv2.moveWindow('picam',0,0)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('gray',705,250)

    if cv2.waitKey(1) == ord ('q'):
        break

cam.release()
cv2.destroyAllWindows()
