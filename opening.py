import cv2
import numpy as np
kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dk=np.array([150,30,30])
    uk=np.array([190,255,255])
    mask=cv2.inRange(hsv,dk,uk)
    son=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)
    cv2.imshow('orjinal',frame)
    cv2.imshow('son', son)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()