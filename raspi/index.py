import cv2
import requests
from datetime import datetime
from deepface import DeepFace

# Open the webcam
cap = cv2.VideoCapture(0)

# Take a picture
ret, image = cap.read()

# Save the image to a file
temp_name = "cap" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
cv2.imwrite("captures/" + temp_name, image)

# Close the webcam
cap.release()

# Analyze the image
result = DeepFace.analyze("captures/" + temp_name, actions = ['age', 'gender', 'race', 'emotion'])

# Print the result
print(result)
print(result['dominant_emotion'])

# Send the image file to the webserver
# url = "http://example.com/upload"
# files = {'image': open('image.jpg', 'rb')}
# r = requests.post(url, files=files)

# print(r.status_code, r.reason)
