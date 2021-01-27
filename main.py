# Tutorial from Programming Hero: https://www.youtube.com/watch?v=AWvsXxDtEkU&t=1267s
from src.Assistant import listen_for_commands, speak
from src.Tools.search import search_web_for
from src import SEARCH_COMMANDS
from src.Tools.youtube import play_youtube_video_for
from src.Tools.process_command import cut_trigger_from_command, get_trigger_word_from
from src.Tools.open import open_page_or_file

import logging

logging.basicConfig(filename='assistant_log.log', level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')


def check_for_trigger_command(trigger: str, command: str):
    is_triggered = bool(trigger.lower() in command.lower())
    logging.debug(f'Searching for trigger command ({trigger}) in command action ({command})')

    if is_triggered:
        command_action = cut_trigger_from_command(trigger, command)
        logging.debug(f'Trigger command ({trigger}) found')
        run_command(command_action)
    return is_triggered


def run_command(command_action):
    phrase, trigger_word = get_trigger_word_from(command_action)

    logging.info(f'Trigger word was {trigger_word}')
    logging.info(f'Phrase was {phrase}')

    if command_action.startswith('play'):
        logging.debug(f'Recognized {trigger_word} as play')
        speak(f'Playing {phrase} on YouTube')
        play_youtube_video_for(phrase)

    elif trigger_word in SEARCH_COMMANDS:
        logging.debug(f'Recognized {trigger_word} as search')
        search_web_for(phrase)
    elif command_action.startswith('open'):
        logging.info(f'Recognized {trigger_word} as open')
        speak(f'Opening {command_action[5:]}')
        logging.info(f'Attempting to open ({command_action[5:]})')

        open_page_or_file(phrase)

    else:
        logging.info(f'Failed to recognize {trigger_word}; reverted to search by default')
        logging.info(f'Attempting to search for {trigger_word}')
        speak(f'The trigger word was {trigger_word}, but I don\'t know what that means.')
        speak(f'I\'ll try to search Google for {phrase}.')
        search_web_for(phrase)


def run_assistant():
    command = listen_for_commands().lower()
    logging.info(f'Checking for trigger word "google" in {command}')
    was_assistant_triggered = check_for_trigger_command("google", command)

    if not was_assistant_triggered:
        logging.debug(f'Assistant not triggered by trigger word.')

        run_command(command)
    else:
        logging.debug(f'Assistant triggered by trigger word.')


if __name__ == '__main__':
    logging.info('Assistant Started ---------------------------------------')
    try:
        run_assistant()
        logging.info('Assistant Stopped ---------------------------------------')
    except Exception as e:
        logging.error(f'Fatal Error reading from microphone {e}')
        logging.warning('Assistant Crashed ---------------------------------------')




