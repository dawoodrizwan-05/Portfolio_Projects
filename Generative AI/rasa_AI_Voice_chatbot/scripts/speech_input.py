import speech_recognition as sr
import requests
from gtts import gTTS
import os
from playsound import playsound

def speech_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    return text

def text_to_speech(response_text):
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

def main():
    while True:
        user_input = speech_to_text()
        print(f"You said: {user_input}")

        # Send recognized text to Rasa server
        rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        payload = {"sender": "user", "message": user_input}
        response = requests.post(rasa_url, json=payload).json()

        if response:
            bot_response = response[0]['text']
            print(f"Bot says: {bot_response}")
            text_to_speech(bot_response)

if __name__ == "__main__":
    main()
