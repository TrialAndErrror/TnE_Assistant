import speech_recognition as sr
import subprocess

from src import listener


def listen_for_commands():
    """
    Listen for command;
    use Google speech detection to extract command;
    then return command

    :return: command: str
    """
    with sr.Microphone() as source:
        print_intro_text()

        voice = listener.listen(source)
        command: str = listener.recognize_google(voice)

        return command


def print_intro_text():
    """
    Clear Screen and display introductory text.
    :return: None
    """
    subprocess.call('clear', shell=True)
    print('Welcome to Ratty\'s Assistant\n'
          '\n'
          '\n'
          'You can ask me to play or look up anything!\n'
          '\n'
          'You can Say:\n'
          '\tSearch for Airline tickets to Florida\n'
          '\tPlay Miley Cyrus - Born in the USA\n'
          '\tWhat is Coronavirus?\n'
          '\tLookup Medical Insurance Prices\n'
          '\tPlay Anthony Fauci Speeches 2020\n'
          '\n'
          '\n'
          'Listening for commands...\n'
          '\n')


