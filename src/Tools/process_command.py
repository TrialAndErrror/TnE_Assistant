import logging
import speech_recognition as sr

from src import listener
from src.Settings import print_custom_intro


def cut_wake_word_from_command(trigger, command):
    """
    Removes trigger from command using string split on the command string.

    Converts command to lowercase.

    Returns the rest of the command string after removing the trigger.

    :param trigger: str
    :param command: str
    :return: str
    """
    command_action = command.split(f' {trigger} ')[1].lower()

    logging.debug(f'Trigger command ({trigger}) removed from ({command})')
    logging.debug(f'Returning {command_action} as command_action')

    return command_action


def get_first_word_and_phrase_from(command_action):
    """
    Split command action on first space;
    assigns first section to phrase and rest to command

    :param command_action: str
    :return: (phrase: str, command: str)
    """
    first_word, phrase = command_action.split(' ', 1)[0], command_action.split(' ', 1)[1]
    logging.debug(f'Removing ({first_word}) from ({command_action})')

    phrase = remove_helper_words(phrase)
    logging.debug(f'Returning ({first_word}), ({phrase}) as first_word, phrase')

    return first_word, phrase


def remove_helper_words(phrase: str):
    """
    Remove 'for', 'to', and 'up' from the beginning of param phrase.
    Removes whitespace before and after removing words.

    Returns cleaned phrase.
    :param phrase: str
    :return: phrase: str
    """
    logging.debug(f'Removing helper words and whitespace from ({phrase})')
    phrase = phrase.strip()
    phrase = phrase[4:] if phrase[:4] == 'for ' else phrase
    phrase = phrase[3:] if phrase[:3] == 'up ' else phrase
    phrase = phrase[3:] if phrase[:3] == 'to ' else phrase
    phrase = phrase.strip()
    logging.debug(f'Removal complete. Returning phrase as ({phrase})')

    return phrase


def listen_for_commands():
    """
    Listen for command;
    use Google speech detection to extract command;
    then return command

    :return: command: str
    """
    with sr.Microphone() as source:
        print_custom_intro()
        voice = listener.listen(source)
        command: str = listener.recognize_google(voice)
        return command
