from src import speak
import pywhatkit


def search_web_for(phrase):
    """
    Confirm search action;
    search content related to param phrase on Google using PyWhatKit.

    :param phrase: str
    :return: None
    """
    speak(f'Let\'s search the web for {phrase}')
    pywhatkit.search(phrase)
