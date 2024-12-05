import cv2 as cv

#kamerayı başlat
cap=cv.VideoCapture(0)


while True:
    ret,frame=cap.read()
    if not ret:
        break
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow('kamera',gray_frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

#kamerayı kapat
cap.release()
cv.destroyAllWindows()