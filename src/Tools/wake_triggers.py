import logging

from src.Settings import ASSISTANT_SETTINGS


def check_for_trigger_command(trigger: str, command: str):
    """
    Check if param trigger is in param command.

    :param trigger: str
    :param command: str
    :return: is_triggered: bool
    """

    logging.debug(f'Searching for trigger word ({trigger}) in command ({command})')
    trigger_test = bool(trigger.lower().startswith(command.lower()))
    if trigger_test:
        logging.debug(f'Assistant triggered by trigger word.')
    else:
        logging.info(f'Assistant not triggered by trigger word.')
    return trigger_test


def set_trigger_command():
    """
    Checks for default wake word in Settings.py.
    By default, the wake word is listed as 'Assistant'

    Returns trigger_command as lowercase string.

    :return: trigger_command: str
    """
    trigger_command = ASSISTANT_SETTINGS.get('Wake Word', 'Assistant')
    return trigger_command.lower()

