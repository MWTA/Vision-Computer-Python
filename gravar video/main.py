# FONTE: http://www.galirows.com.br/meublog/opencv-python/opencv2-python27/capitulo1-basico/mostrar-webcam-video/

import cv2

captura = cv2.VideoCapture(0)

while(1):
    ret, frame = captura.read()

    (b, g, r) = frame[200, 200]
    frame[198:202, 198:202] = (0, 0, 255)
    frame[10:90, 10:90] = (b, g, r)
       
    cv2.imshow('frame',frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()