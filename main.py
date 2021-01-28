from src.Assistant import run_assistant

import logging

logging.basicConfig(filename='assistant_log.log', level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')


def run_assistant_with_logging():
    """
    Write start and stop lines in logs for ease of reading.

    Runs assistant in try block with error logging if it crashes.

    If you manually stop the process, you'll likely trigger an exception here;
    those can be ignored if they are user-created.

    :return: None
    """
    logging.info('Assistant Started ---------------------------------------')
    try:
        run_assistant()
        logging.info('Assistant Stopped ---------------------------------------')
    except Exception as e:
        logging.error(f'Fatal Error reading from microphone {e}')
        logging.warning('Assistant Crashed ---------------------------------------')


if __name__ == '__main__':
    run_assistant_with_logging()




