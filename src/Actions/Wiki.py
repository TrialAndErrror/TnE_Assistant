import pywhatkit
import wikipedia
from urllib.parse import quote
from src.Tools.process_command import remove_helper_words
from src import speak
import webbrowser

from src.Settings import WIKI_SETTINGS


def check_for_wiki_commands(phrase: str):
    open_wiki_url(phrase)

    read_wiki_summary(phrase)

    wiki_command_found = True

    return wiki_command_found


def open_wiki_url(phrase):
    web_phrase = quote(phrase).capitalize()
    webbrowser.open(f'https://en.wikipedia.org/wiki/{web_phrase}')


def read_wiki_summary(phrase):
    speak(f'Here\'s what I found on Wikipedia for {phrase}:')

    response = wikipedia.summary(phrase, WIKI_SETTINGS['Lines to Read'])
    speak(response)


def search_wiki_for(phrase):
    """
    Confirm search action;
    search content related to param phrase on Google using PyWhatKit.

    :param phrase: str
    :param trigger_word: str
    :return: None
    """
    phrase = remove_helper_words(phrase)

    wiki_command_found = check_for_wiki_commands(phrase)
    if not wiki_command_found:
        speak(f'Let\'s search the web for {phrase}')
        pywhatkit.search(phrase)
