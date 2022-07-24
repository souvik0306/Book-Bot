import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode 

frame = cv.imread(r'D:\Book-Bot New\Book-Bot\Media\qr.png')
frame = cv.resize(frame,(300,300))
for barcode in decode(frame):
    print(barcode.data.decode('utf-8'))
    Data = barcode.data.decode('utf-8')
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((1,-1,2))
    cv.polylines(frame,[pts],True,(0,255,0),3)
    pts2 = barcode.rect
    cv.putText(frame,Data,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX_SMALL,0.9,(255,0,255),2)
cv.imshow("Frame",frame)
cv.waitKey(0)
cv.destroyAllWindows()
