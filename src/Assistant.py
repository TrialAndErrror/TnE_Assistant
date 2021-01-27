import speech_recognition as sr

from src import engine, listener


def listen_for_commands():

    with sr.Microphone() as source:
        print_intro_text()

        voice = listener.listen(source)
        command: str = listener.recognize_google(voice)

        return command


def print_intro_text():
    print('\n' * 100)
    print('Welcome to Ratty\'s Assistant')
    print('\n\nYou can ask me to play or look up anything!\n\n')
    print('You can Say:')
    print('\tSearch for Airline tickets to Florida')
    print('\tPlay Miley Cyrus - Born in the USA')
    print('\tWhat is Coronavirus?')
    print('\tLookup Medical Insurance Prices')
    print('\tPlay Anthony Fauci Speeches 2020')
    print('\n\nListening for commands...\n\n')


# english-north


def set_voice():
    engine.setProperty('voice', "english")


def speak(phrase):
    engine.say(phrase)
    engine.runAndWait()
