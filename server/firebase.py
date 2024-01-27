import requests
import json

api_url = 'http://127.0.0.1:5000/move_servo'

# Data to be sent in the POST request
data = {
    'pin': 3,  # Replace with the actual pin value
    'angle': 90  # Replace with the actual angle value
}

# Send the POST request
response = requests.post(api_url, json=data)

# Print the response
print(response.json())