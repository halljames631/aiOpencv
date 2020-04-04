import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    frame = cv2.rectangle(frame,(140,100),(200,130),(255,0,0),3)
    fnt = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame,"my first text",(300,300),fnt,1,(255,0,0),2)
    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)

    if cv2.waitKey(1) == ord ('q'):
        break

cam.release()
cv2.destroyAllWindows()