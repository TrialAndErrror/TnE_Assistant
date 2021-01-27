import pywhatkit

from src.Tools.process_command import remove_for_from
from src.Tools.wiki import check_for_wiki_commands
from src import engine


def search_web_for(phrase):
    phrase = remove_for_from(phrase)
    wiki_command_found = check_for_wiki_commands(phrase)

    if not wiki_command_found:
        engine.say(f'Let\'s see what\'s on Google for {phrase}')
        engine.runAndWait()
        pywhatkit.search(phrase)


