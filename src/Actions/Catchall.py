import logging

from src import speak
from src.Actions.Search import search_web_for


def do_catchall_action(phrase, trigger_word):
    """
    Log that the trigger word was not recognized, then perform default action.

    Default: Search

    :param phrase: str
    :param trigger_word: str
    :return:
    """
    logging.info(f'Failed to recognize {trigger_word}; reverted to search by default')
    speak(f'The trigger word was {trigger_word}, but I don\'t know what that means.')

    """
    Below is the catchall action to do when the command is not recognized.
    By default, it is set to search the web for the phrase.
    """
    speak(f'I\'ll try to search Google for {phrase}.')
    search_web_for(phrase)
