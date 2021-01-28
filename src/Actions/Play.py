import pywhatkit
from src import speak


def play_youtube_video_for(phrase):
    """
    Confirm play action;
    play content related to param phrase on YouTube using PyWhatKit.

    :param phrase: str
    :param trigger_word: str
    :return: None
    """
    speak(f'Playing {phrase} on YouTube')
    pywhatkit.playonyt(phrase)
