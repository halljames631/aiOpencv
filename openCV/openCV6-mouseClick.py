import cv2

print(cv2.__version__)
evt = -1
def click(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pnt 
        global evt
        print('mouse event was: ', event)
        print(x,',',y)
        pnt = (x,y)
        evt = event

cv2.namedWindow('picam')
cv2.setMouseCallback('picam',click)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if evt == 1:
        cv2.circle(frame,pnt,5,(0,0,255),-1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        myStr = str(pnt)
        cv2.putText(frame,myStr,pnt,font,1,(255,0,0),2)

    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)

    if cv2.waitKey(1) == ord ('q'):
        break

cam.release()
cv2.destroyAllWindows()
