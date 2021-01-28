import pywhatkit
import logging
from src import speak


def play_youtube_video_for(phrase, trigger_word):
    logging.debug(f'Recognized {trigger_word} as play')
    speak(f'Playing {phrase} on YouTube')
    pywhatkit.playonyt(phrase)
