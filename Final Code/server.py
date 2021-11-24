# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:56:55 2021

@author: Ratnadeep Das Choudhury
"""

from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request

import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode 

app = Flask(__name__)

app.secret_key="secretkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/IotProject"

mongo = PyMongo(app)

studentQR = 0
bookBarcode = 0
warn = "Scan both QR code and Book Barcode"
success = "Submitted successfully"

@app.route('/')
def index():
  return render_template('codeScanner.html')

@app.route('/studentQR/')
def codeScanner():
    cap = cv.VideoCapture(0)

    while True:
        _,frame = cap.read()
    
        for barcode in decode(frame):
            print(barcode.data.decode('utf-8'))
            global studentQR
            studentQR = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((1,-1,2))
            cv.polylines(frame,[pts],True,(0,255,0),3)
            pts2 = barcode.rect
            cv.putText(frame,studentQR,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX_SMALL,0.9,(255,0,255),2)
            # scanned = mongo.db.scanned.insert_one({"scanned": studentQR})
            
            return studentQR
            
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == 27:  # Press Escape Key to close all windows
            break
    cap.release()
    cv.destroyAllWindows()

@app.route('/BookBarcode/')
def barcodeScanner():
    cap = cv.VideoCapture(0)

    while True:
        _,frame = cap.read()
    
        for barcode in decode(frame):
            print(barcode.data.decode('utf-8'))
            global bookBarcode
            bookBarcode = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((1,-1,2))
            cv.polylines(frame,[pts],True,(0,255,0),3)
            pts2 = barcode.rect
            cv.putText(frame,bookBarcode,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX_SMALL,0.9,(255,0,255),2)
            
            return bookBarcode
            
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == 27:  # Press Escape Key to close all windows
            break
    cap.release()
    cv.destroyAllWindows()

@app.route('/Submit/')
def submit():
  global studentQR 
  global bookBarcode
  if studentQR !=0 and bookBarcode != 0:
    scanned = mongo.db.scanned.insert_one({"Student Id": studentQR, "Book Barcode": bookBarcode})
    studentQR=0
    bookBarcode=0
    return success
  else:
    return warn

# @app.route('/records')
# def record():
#   recordItem = mongo.db.scanned.find()
#   resp = dumps(recordItem)
#   return resp

if __name__ == '__main__':
  app.run(debug=True)