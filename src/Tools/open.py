import webbrowser
from src import engine


def open_page_or_file(phrase):
    if phrase == 'mail':
        open_mail_link()
    else:
        engine.say(f'I don\'t know how to open {phrase}')
        engine.runAndWait()


def open_mail_link():
    mail_url = 'https://mail.google.com/mail/u/0/'
    webbrowser.open(mail_url)
