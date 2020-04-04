import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)
outVid = cv2.VideoWriter('videos/myCam.avi',cv2.VideoWriter_fourcc(*'XVID'),30,(640,480))

while True:
    ret, frame = cam.read()

    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)
    outVid.write(frame)

    if cv2.waitKey(1) == ord ('q'):
        break


cam.release()
outVid.release()
cv2.destroyAllWindows()
