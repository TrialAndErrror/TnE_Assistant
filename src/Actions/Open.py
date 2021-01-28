import webbrowser

from src import speak
from src.Settings import ASSISTANT_SETTINGS


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
    """
    Get mail url from Settings file, then open in web browser.

    Defaults to GMail if nothing provided in settings.
    :return: None
    """
    default_url = 'https://mail.google.com/mail/u/0/'
    mail_url = ASSISTANT_SETTINGS.get('Mail URL', default_url)
    webbrowser.open(mail_url)
