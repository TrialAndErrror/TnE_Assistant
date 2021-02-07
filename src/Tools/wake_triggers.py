import logging

from src.Settings import ASSISTANT_SETTINGS


def check_for_wake_word(command: str):
    """
    Check if wake word is in param command.

    :param command: str
    :return: is_triggered: bool
    """
    wake_word: str = ASSISTANT_SETTINGS.get('Wake Word')

    logging.debug(f'Searching for wake word ({wake_word}) in command ({command})')
    wake_word_found = bool(command.lower().startswith(wake_word.lower()))
    if wake_word_found:
        logging.debug(f'Assistant activated by wake word.')
    else:
        logging.info(f'Assistant not activated by wake word.')
    return wake_word_found


def get_trigger_command():
    """
    Checks for default wake word in Settings.py.
    By default, the wake word is listed as 'Assistant'

    Returns trigger_command as lowercase string.

    :return: trigger_command: str
    """
    trigger_command = ASSISTANT_SETTINGS.get('Wake Word', 'assistant')
    return trigger_command.lower()

