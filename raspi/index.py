import cv2
from datetime import datetime
from playsound import playsound





def snap_and_save_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Take a picture
    ret, image = cap.read()

    # Save the image to a file
    temp_name = "cap" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    cv2.imwrite("captures/" + temp_name, image)

    # Close the webcam
    cap.release()

    return "captures/" + temp_name


def sound_results(img_info):

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
    # img_path = snap_and_save_image()
    img_info = {"dominant_emotion" : "happy",
                "gender" : "Man",
                "age" : 18
                }
    sound_results(img_info)