import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dk=np.array([150,30,30])
    uk=np.array([190,255,255])
    dm=np.array([0,0,0])
    um=np.array([0,255,190])
    mask=cv2.inRange(hsv,dk,uk)
    son=cv2.bitwise_and(frame,frame,mask=mask)
    mask2=cv2.inRange(hsv,dm,um)
    son2=cv2.bitwise_and(frame,frame,mask=mask2)
    cv2.imshow('orjinal',frame)
    cv2.imshow('son', son)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()