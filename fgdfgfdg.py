import cv2
kamera=cv2.VideoCapture(0)
while True:
    ret, frame=kamera.read()
    cv2.imshow('goruntu', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()