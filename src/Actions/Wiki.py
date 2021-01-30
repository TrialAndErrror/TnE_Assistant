import wikipedia
from urllib.parse import quote
from src import speak
import webbrowser

from src.Settings import WIKI_SETTINGS


def open_wiki_url(phrase: str):
    """
    Capitalize and parse phrase as web-friendly string;
    open web browser to Wikipedia page for web-friendly string

    :param phrase: str
    :return: None
    """
    webbrowser.open(f'https://en.wikipedia.org/wiki/{quote(phrase.capitalize())}')


def read_wiki_summary(phrase, lines_to_read):
    """
    Read specific number of lines from the Summary of phrase on Wikipedia

    :param phrase: str
    :param lines_to_read: int
    :return: None
    """
    response = wikipedia.summary(phrase, lines_to_read)
    speak(f'Here\'s what I found on Wikipedia for {phrase}: {response}')


def open_wiki_results_for(phrase):
    """
    Open Wiki URL for phrase;
    Read Wiki summary aloud based on number of lines specified in Settings.

    :param phrase: str
    :return: None
    """
    open_wiki_url(phrase)

    lines_to_read: int = WIKI_SETTINGS.get('Lines to Read', 1)
    read_wiki_summary(phrase, lines_to_read)

