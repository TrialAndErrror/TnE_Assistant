import logging

from src.Assistant import perform_action
from src.Settings import ASSISTANT_SETTINGS
from src.Tools.process_command import cut_trigger_from_command


def check_for_trigger_command(trigger: str, command: str):
    """
    Check if param trigger is in param command.

    :param trigger: str
    :param command: str
    :return: is_triggered: bool
    """

    logging.debug(f'Searching for trigger word ({trigger}) in command action ({command})')
    is_triggered = bool(trigger.lower().startswith(command.lower()))

    if is_triggered:
        command_action = cut_trigger_from_command(trigger, command)
        perform_action(command_action)
    return is_triggered


def set_trigger_command():
    """
    Checks for default wake word in Settings.py.

    If not found, returns None.

    If found, returns trigger_command as lowercase string.

    :return: trigger_command: str
    """
    trigger_command = ASSISTANT_SETTINGS.get('Wake Word', None)
    if trigger_command:
        return trigger_command.lower()
