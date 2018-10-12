import cv2
import numpy as np

img=cv2.imread('sayfa.jpg')
ret, threshold=cv2.threshold(img,10,255,cv2.THRESH_BINARY)

griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gauss =cv2.adaptiveThreshold(griton,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('orjinal',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gauss',gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()

