# write code to move a servo with pyfirmata
import serial
import serial.tools.list_ports
from pyfirmata import Arduino, SERVO, util
import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

# python -m flask --app main run

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

# Specify the port where your Arduino is connected
arduino_port = 'COM8'  # Example port on Windows

# Create a PyFirmata board
board = Arduino(arduino_port)

# Attach the servo to pin 9 (adjust the pin number based on your setup)
servo_pin = 9
servo = board.digital[servo_pin]
servo.mode = SERVO

# Function to move the servo to a specific angle
def move_servo(angle):
    print("Moving servo to {} degrees".format(angle))
    servo.write(angle)
    # for i in range(0, angle, 1):
    #     servo.write(i)
    #     time.sleep(0.0015)
    
# Move the servo back and forth between 0 and 180 degrees
move_servo(180)

while True:
    num = input("Enter an angle between 0 and 180 degrees: ")
    move_servo(int(num))

# Close the serial connection
# board.exit()






