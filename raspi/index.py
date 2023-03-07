import cv2
from datetime import datetime
from playsound import playsound
import requests as req


URL = "http://localhost:5000"


def upload_image_to_firebase(img_path):
    # Upload the image to firebase
    # TODO: Implement this function
    pass

def make_request_to_server(img_path):

    # Send the image to the server
    files = {'file': open(img_path, 'rb')}
    print("sending post request to server")
    r = req.post(f"{URL}/analyze", files=files)

    # Get the response from the server

    response = r.json()
    print("got response from server")
    print(response)

    # Return the response
    return response




def snap_and_save_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    print("Webcam opened")

    # Take a picture
    ret, image = cap.read()
    print("snapped image")

    # Save the image to a file
    temp_name = "cap" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(temp_name, image)
    print(f"saved image to {temp_name}")

    # Close the webcam
    cap.release()
    print("Webcam closed")

    return temp_name


def sound_results(img_info):

    if(img_info["error"]):
        playsound("sounds/error.mp3")
        return
    
    print("playing sound for info:")
    print(img_info)

    play_emotion_sound(img_info["dominant_emotion"])
    play_gender_sound(img_info["gender"])
    play_age_sound(img_info["age"])

    

def play_age_sound(age):
    print(age)
    if(age < 18):
        playsound("sounds/age/under18.mp3")
    elif(age >= 18 and age < 30):
        playsound("sounds/age/18to30.mp3")
    elif(age >= 30 and age < 50):
        playsound("sounds/age/30to50.mp3")
    elif(age >= 50):
        playsound("sounds/age/over50.mp3")
    else:
        print("no age detected")

def play_gender_sound(gender):
    print(gender)
    if(gender == "Man"):
        playsound("sounds/gender/Man.mp3")
    elif(gender == "Woman"):
        playsound("sounds/gender/Woman.mp3")
    else:
        print("no gender detected")


def play_emotion_sound(emotion):
    print(emotion)
    if(emotion == "angry"):
        playsound("sounds/emotion/angry.mp3")
    elif(emotion == "disgust"):
        playsound("sounds/emotion/disgust.mp3")
    elif(emotion == "fear"):
        playsound("sounds/emotion/fear.mp3")
    elif(emotion == "happy"):
        playsound("sounds/emotion/happy.mp3")
    elif(emotion == "sad"):
        playsound("sounds/emotion/sad.mp3")
    elif(emotion == "surprise"):
        playsound("sounds/emotion/surprise.mp3")
    elif(emotion == "neutral"):
        playsound("sounds/emotion/neutral.mp3")
    else:
        print("No emotion detected")



if __name__ == "__main__":
    img_path = snap_and_save_image()
    img_info = make_request_to_server(img_path)
    sound_results(img_info)
    upload_image_to_firebase(img_path)
    