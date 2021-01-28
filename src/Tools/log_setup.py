import logging
import os

from src.Assistant import run_assistant
from src.Settings import DEBUG_LOGGING_ENABLED


def run_assistant_with_logging():
    """
    Setup logging based on DEBUG_LOGGING_ENABLED in Settings.

    Write start and stop lines in logs for ease of reading.

    Runs assistant in try block with error logging if it crashes.

    If you manually stop the process, you'll likely trigger an exception here;
    those can be ignored if they are user-created.

    :return: None
    """
    setup_log_dir()
    set_logging_level()
    logging.info('Assistant Started ---------------------------------------')

    try:
        run_assistant()
        logging.info('Assistant Stopped ---------------------------------------')

    except Exception as e:
        logging.error(f'Fatal Error reading from microphone {e}')
        logging.warning('Assistant Crashed ---------------------------------------')


def set_logging_level():
    """
    Check Settings if Debug Logging is enabled and set the appropriate logging level.

    :return: None
    """
    if DEBUG_LOGGING_ENABLED:
        logging.basicConfig(
            filename='logs/assistant_debug_log.log',
            level=logging.DEBUG,
            format='%(levelname)s:%(asctime)s:%(message)s'
        )
    else:
        logging.basicConfig(
            filename='logs/assistant_error_log.log',
            level=logging.WARNING,
            format='%(levelname)s:%(asctime)s:%(message)s'
        )


def setup_log_dir():
    """
    Get log path based on current working directory;
    make directory if it does not exist.

    :return: None
    """
    log_path = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
