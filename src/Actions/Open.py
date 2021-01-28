import webbrowser

from src import speak
from src.Settings import set_mail_url


def open_page_or_file(phrase):
    """
    Handles all routes based on the 'Open' first_word.

    Currently only supports opening custom e-mail link.

    Links defined in Settings.

    :param phrase: str
    :return: None
    """
    if phrase == 'mail':
        speak(f'Opening Mail')
        open_mail_link()
    else:
        speak(f'I don\'t know how to open {phrase}')


def open_mail_link():
    mail_url = set_mail_url()
    webbrowser.open(mail_url)
