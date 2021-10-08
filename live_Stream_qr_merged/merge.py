# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:56:55 2021

@author: ratnadeep das choudhury
"""
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode 
from camera import VideoCamera
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os

def my_link():
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
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == 27:  # Press Escape Key to close all windows
            break
    cap.release()
    cv.destroyAllWindows()

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


