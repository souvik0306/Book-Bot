import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode 

cap = cv.VideoCapture(0)

while True:
    _,frame = cap.read()

    for barcode in decode(frame):
        print(barcode.data.decode('utf-8'))
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((1,-1,2))
        cv.polylines(frame,[pts],True,(0,255,0),3)
        
    cv.imshow("Frame",frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv.destroyAllWindows()
