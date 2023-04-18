
from flask import Flask, jsonify, make_response
import subprocess
import cv2
import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
import base64

img = cv2.imread('/Users/furkankose/Desktop/count/PPC0.jpeg')
 
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#________________________
box, label, count = cv.detect_common_objects(img)
people_count = 0
for i in range(len(label)):
    if label[i] == "person":
        draw_bbox(img, [box[i]], [label[i]], 1)
        people_count += 1

output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, buffer = cv2.imencode('.jpg', output)
jpg_as_text = base64.b64encode(buffer).decode('utf-8')
 
app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(f'<h1>Number of people: {people_count}</h1><img src="data:image/jpeg;base64,{jpg_as_text}" />')
    response.headers.set('Content-Type', 'text/html')
    return response

if __name__ == '__main__':
    app.run()

