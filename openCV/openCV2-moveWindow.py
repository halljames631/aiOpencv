import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('picamGray',gray)
    cv2.moveWindow('picamGray',0,550)
    if cv2.waitKey(1) == ord ('q'):
        break

cam.release()
cv2.destroyAllWindows()