import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

from src.Assistant import set_voice  # noqa:E402

set_voice()
SEARCH_COMMANDS = [
    'what',
    'look',
    'lookup',
    'find',
    'search',
    'who'
]