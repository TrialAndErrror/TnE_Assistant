import webbrowser
import logging

from src import speak


def open_page_or_file(phrase, trigger_word):
    logging.info(f'Recognized {trigger_word} as open; attempting to open {phrase[5:]}')
    speak(f'Opening {phrase[5:]}')

    if phrase == 'mail':
        open_mail_link()
    else:
        speak(f'I don\'t know how to open {phrase}')


def open_mail_link():
    mail_url = 'https://mail.google.com/mail/u/0/'
    webbrowser.open(mail_url)
