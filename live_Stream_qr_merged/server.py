# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:56:55 2021

@author: ratnadeep das choudhury
"""

from flask import Flask, render_template
app = Flask(__name__)

import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode 

@app.route('/')
def index():
  return render_template('codeScanner.html')

@app.route('/codeScanner/')
def codeScanner():
    cap = cv.VideoCapture(0)

    while True:
        _,frame = cap.read()
    
        for barcode in decode(frame):
            print(barcode.data.decode('utf-8'))
            Data = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((1,-1,2))
            cv.polylines(frame,[pts],True,(0,255,0),3)
            pts2 = barcode.rect
            cv.putText(frame,Data,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX_SMALL,0.9,(255,0,255),2)
            # return Data
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == 27:  # Press Escape Key to close all windows
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
  app.run(debug=True)