import pywhatkit
import wikipedia
from urllib.parse import quote
from src.Tools.process_command import remove_helper_words
from src import speak
import webbrowser

from src.Settings import WIKI_SETTINGS


def open_wiki_url(phrase):
    web_phrase = quote(phrase).capitalize()
    webbrowser.open(f'https://en.wikipedia.org/wiki/{web_phrase}')


def read_wiki_summary(phrase):
    lines_to_read = WIKI_SETTINGS['Lines to Read']
    response = wikipedia.summary(phrase, lines_to_read)

    speak(f'Here\'s what I found on Wikipedia for {phrase}:')
    speak(response)


def search_wiki_for(phrase):
    """
    Confirm search action;
    search content related to param phrase on Google using PyWhatKit.

    :param phrase: str
    :return: None
    """
    open_wiki_url(phrase)
    read_wiki_summary(phrase)

