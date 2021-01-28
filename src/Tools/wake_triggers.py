import logging

from src.Settings import ASSISTANT_SETTINGS


def check_for_wake_word(wake_word: str, command: str):
    """
    Check if param trigger is in param command.

    :param wake_word: str
    :param command: str
    :return: is_triggered: bool
    """

    logging.debug(f'Searching for wake word ({wake_word}) in command ({command})')
    wake_word_found = bool(wake_word.lower().startswith(command.lower()))
    if wake_word_found:
        logging.debug(f'Assistant activated by wake word.')
    else:
        logging.info(f'Assistant not activated by wake word.')
    return wake_word_found


def set_trigger_command():
    """
    Checks for default wake word in Settings.py.
    By default, the wake word is listed as 'Assistant'

    Returns trigger_command as lowercase string.

    :return: trigger_command: str
    """
    trigger_command = ASSISTANT_SETTINGS.get('Wake Word', 'assistant')
    return trigger_command.lower()

