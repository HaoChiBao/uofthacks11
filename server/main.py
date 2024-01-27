import serial
import serial.tools.list_ports

from pyfirmata import Arduino, SERVO, util
import time

from flask import Flask, request, jsonify

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


# ser.close()


