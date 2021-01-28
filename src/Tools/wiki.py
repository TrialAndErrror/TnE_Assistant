import wikipedia
from urllib.parse import quote
from src.Tools.process_command import remove_helper_words
from src import engine
import webbrowser


def check_for_wiki_commands(phrase: str):
    wikipedia_commands = ['wikipedia', 'who is', 'what is']

    wiki_command_found = False

    for command in wikipedia_commands:
        if phrase.startswith(command):

            phrase = process_wiki_phrase(command, phrase)

            print(f'Seaching Wikipedia for {phrase}')
            engine.say(f'Here\'s what I found on Wikipedia for {phrase}:')
            open_wiki_url(phrase)
            engine.runAndWait()
            read_wiki_summary(phrase)

            wiki_command_found = True

            break
    return wiki_command_found


def open_wiki_url(phrase):
    web_phrase = quote(phrase).capitalize()
    webbrowser.open(f'https://en.wikipedia.org/wiki/{web_phrase}')


def read_wiki_summary(phrase):
    num_lines_to_read = 1
    response = wikipedia.summary(phrase, num_lines_to_read)
    engine.say(response)
    engine.runAndWait()


def process_wiki_phrase(command, phrase):
    phrase = phrase.replace(f'{command}', '')
    phrase = remove_helper_words(phrase)
    return phrase
