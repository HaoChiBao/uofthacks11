import cv2
from deepface import DeepFace
import numpy as np

import requests
import json

firebase_config = {
    "apiKey": "AIzaSyA5_6MeslRHd-zTd2xiqYKUpsajf4GmxQY",
    "authDomain": "uofthacks11-3aaad.firebaseapp.com",
    "projectId": "uofthacks11-3aaad",
    "storageBucket": "uofthacks11-3aaad.appspot.com",
    "messagingSenderId": "638732020721",
    "appId": "1:638732020721:web:69cdc8ef8d4f6f2d953250"
}

db_url = 'https://uofthacks11-3aaad-default-rtdb.firebaseio.com/'

def get_data():
    url = db_url + '/expression.json'
    response = requests.get(url)
    return response.json()

def post_data(data):
    url = db_url + '/expression.json'
    response = requests.put(url, data=json.dumps(data))
    return response.json()

def move_servo(data):
    api_url = 'http://127.0.0.1:5000/move_servo'

    # Send the POST request
    response = requests.post(api_url, json=data)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)


minY = 40
maxY = 120
angleX = 90
angleY = 90

while video.isOpened():
    _, frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    
    for x,y,w,h in face:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        try:
            analyze = DeepFace.analyze(img, actions=['emotion'])
            # print(analyze)
            emotion = analyze[0]['dominant_emotion']
            print(emotion)
            post_data({'expression': emotion})
            
            # get mid point of face
            mid_x = x + w/2
            mid_y = y + h/2
            
            # get mid point of frame
            frame_x = frame.shape[1]/2
            frame_y = frame.shape[0]/2
            
            # get difference
            diff_x = mid_x - frame_x
            diff_y = mid_y - frame_y
            
            # get percentage
            per_x = diff_x / frame_x
            per_y = diff_y / frame_y
            
            if(per_x > 0.1):
                print('move right')
                if(angleX < 0):
                    continue
                angleX -= 5
                move_servo({'pin': 3, 'angle': angleX})
                
            if(per_x < -0.1):
                print('move left')
                if(angleX > 180):
                    continue
                angleX += 5
                move_servo({'pin': 3, 'angle': angleX})
                
            if(per_y > 0.1):
                print('move down')
                if angleY < minY:
                    continue
                angleY -= 5
                move_servo({'pin': 9, 'angle': angleY})
            
            if(per_y < -0.1):
                print('move up')
                if angleY > maxY:
                    continue
                angleY += 5
                move_servo({'pin': 9, 'angle': angleY})
            
            
            
            
        except Exception as e:
            print('no face')
            post_data({'expression': 'no face'})
        
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
video.release()