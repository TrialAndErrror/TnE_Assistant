from src import speak
from src.Actions.Search import search_web_for


def do_catchall_action(phrase, command_word):
    """
    Log that the trigger word was not recognized, then perform default action.

    Default: Search

    :param phrase: str
    :param command_word: str
    :return:
    """
    speak(f'The command word was {command_word}, but I don\'t know what that means.')
    speak(f'I\'ll try to search Google for {phrase}.')
    search_web_for(phrase)
