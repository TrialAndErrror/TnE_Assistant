import speech_recognition as sr
import pyttsx3

SEARCH_COMMANDS = [
    'what',
    'look',
    'lookup',
    'find',
    'search',
    'who'
]

listener = sr.Recognizer()
engine = pyttsx3.init()


def speak(phrase):
    engine.say(phrase)
    engine.runAndWait()


def set_voice():
    """
    Set voice to English by default.

    Can modify the chosen_voice variable to set a different default voice.

    :return: None
    """
    chosen_voice = "english"
    engine.setProperty('voice', chosen_voice)


set_voice()



