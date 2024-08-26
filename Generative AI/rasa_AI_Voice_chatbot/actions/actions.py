from gtts import gTTS
import os
from playsound import playsound
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTextToSpeech(Action):

    def name(self) -> str:
        return "action_text_to_speech"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        response = tracker.latest_message['text']
        tts = gTTS(text=response, lang='en')
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")

        dispatcher.utter_message(text=response)
        return []
