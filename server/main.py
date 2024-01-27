import serial
import serial.tools.list_ports

from pyfirmata import Arduino, SERVO, util
import time

from flask import Flask, request, jsonify

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



ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

# python -m flask --app main run

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

# Define the serial port and baud rate
port = 'COM8'  # Change 'COMx' to your Arduino's serial port (e.g., COM3 or /dev/ttyUSB0)
board = Arduino(port)
# exit(0)

app = Flask(__name__)

@app.route('/')
def index():
    print('index')
    return 'default msg'

@app.route('/move_servo', methods=['POST'])
def servo():
    data = request.get_json()
    print(data)
    
    if 'pin' not in data:
        return jsonify({'error': 'pin is not defined'})
    
    if 'angle' not in data:
        return jsonify({'error': 'angle is not defined'})
    
    # return jsonify(request.json)
    
    pin = data['pin']
    angle = data['angle']
    
    
    print('pin: ' + str(pin))
    print('angle: ' + str(angle))
    
    # Initialize the serial connection
    servo = board.digital[pin]
    servo.mode = SERVO
    
    servo.write(angle)
    time.sleep(0.015)
    
    
    return jsonify(request.json)

@app.route('/get_emotion', methods=['GET'])
def emotion():
    data = get_data()
    print(data)
    return jsonify(data)