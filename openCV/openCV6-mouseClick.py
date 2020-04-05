import cv2
import numpy as np

print(cv2.__version__)
evt = -1
coord = []
img = np.zeros((250,250,3),np.uint8)

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
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        blue = frame[y,x,0]
        green = frame[y,x,1]
        red = frame[y,x,2]
        print(blue,green,red)
        colorString = str(blue) + ',' + str(green) + ',' + str(red)
        img[:] = [blue,green,red]
        fnt = cv2.FONT_HERSHEY_PLAIN
        r = 255 - int(red)
        g = 255 - int(green)
        b = 255 - int(blue)
        tp = (b,g,r)
        cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
        cv2.imshow('mycolor',img)

cv2.namedWindow('picam')
cv2.setMouseCallback('picam',click)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,0,255),-1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        myStr = str(pnts)
        cv2.putText(frame,myStr,pnts,font,1,(5,5,5),2)

    cv2.imshow('picam', frame)
    cv2.moveWindow('picam',0,0)

    keyEvent = cv2.waitKey(1)

    if keyEvent == ord ('q'):
        break

    if keyEvent == ord('c'):
        coord.clear()

cam.release()
cv2.destroyAllWindows()
