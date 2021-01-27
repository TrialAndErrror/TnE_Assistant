import webbrowser
from src import engine


def open_page_or_file(phrase):
    if phrase == 'mail':
        webbrowser.open('https://mail.google.com/mail/u/0/')
    else:
        engine.say(f'I don\'t know how to open {phrase}')
