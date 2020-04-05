import cv2

print(cv2.__version__)
evt = -1
coord = []
def click(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pnt 
        global evt
        print('mouse event was: ', event)
        print(x,',',y)
        pnt = (x,y)
        coord.append(pnt)
        print(coord)
        evt = event

cv2.namedWindow('picam')
cv2.setMouseCallback('picam',click)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,0,255),-1)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # myStr = str(pnt[pnts])
        # cv2.putText(frame,myStr,pnts[pnts],font,1,(255,0,0),2)

    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)

    keyEvent = cv2.waitKey(1)

    if keyEvent == ord ('q'):
        break

    if keyEvent == ord('c'):
        coord.clear()

cam.release()
cv2.destroyAllWindows()
