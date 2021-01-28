
import speech_recognition as sr
import subprocess
import logging

from src import listener
from src.Actions.Open import open_page_or_file
from src.Actions.Play import play_youtube_video_for
from src.Actions.Search import search_web_for
from src.Actions.Wiki import search_wiki_for
from src.Settings import print_custom_intro, WIKI_SETTINGS, SEARCH_COMMANDS
from src.Tools.process_command import get_first_word_and_phrase_from
from src.Tools.wake_triggers import check_for_trigger_command, set_trigger_command
from src.Actions.Catchall import do_catchall_action
from src.Settings import DEBUG_LOGGING_ENABLED


def listen_for_commands():
    """
    Listen for command;
    use Google speech detection to extract command;
    then return command

    :return: command: str
    """
    with sr.Microphone() as source:
        print_intro_text()

        voice = listener.listen(source)
        command: str = listener.recognize_google(voice)

        return command


def print_intro_text():
    """
    Clear Screen and display introductory text.
    :return: None
    """
    subprocess.call('clear', shell=True)
    print_custom_intro()


def run_assistant():
    """
    Listen for commands;
    check whether trigger command was
    :return:
    """
    command = listen_for_commands().lower()

    """
    set_trigger_command is a function in the user file which allows you to set a keyword to trigger the assistant.
    """
    trigger_command = set_trigger_command()
    logging.info(f'Checking for trigger word {trigger_command} in {command}')
    was_assistant_triggered = check_for_trigger_command(trigger_command, command)

    if not was_assistant_triggered:
        logging.debug(f'Assistant not triggered by trigger word.')

        perform_action(command)
    else:
        logging.debug(f'Assistant triggered by trigger word.')


def perform_action(command_action):
    """
    Get First Word and Phrase from command,
    then process accordingly.

    :param command_action: str
    :return: None
    """

    first_word, phrase = get_first_word_and_phrase_from(command_action)

    """
    Get first word and phrase. 
    'phrase' has had helper words removed and whitespace stripped.
    
    Then, check first word against available Actions below:
    """

    if first_word == 'play':

        """
        Option 1: "Play"
        Play using pywhatkit.playonyt()
        """

        logging.debug(f'Recognized {first_word} as Play; playing {phrase}')
        play_youtube_video_for(phrase)

    elif first_word in WIKI_SETTINGS['Commands']:

        """
        Option 2: "Who/What/Wiki"
        Read Wikipedia using wikipedia.summary()
        Open web browser to Wikipedia website
        """

        logging.debug(f'Recognized {first_word} as Wiki; searching Wiki for {phrase}')
        search_wiki_for(phrase)

    elif first_word in SEARCH_COMMANDS:

        """
        Option 3: "Search/Find/Google/Lookup"
        Search on Google using pywhatkit.search()
        """

        logging.debug(f'Recognized {first_word} as Search; searching Google for {phrase}')
        search_web_for(phrase)

    elif first_word == 'open':

        """
        Option 4: "Open"
        Open various locations;
        currently limited to e-mail only based on url in Settings
        """

        logging.info(f'Recognized {first_word} as open; attempting to open {phrase[5:]}')
        open_page_or_file(phrase)

    else:

        """
        Catchall Option:
        When the first word is not recognized, Assistant goes here.
        Currently set to Google Search by default.
        """

        do_catchall_action(phrase, first_word)


def run_assistant_with_logging():
    """
    Setup logging based on DEBUG_LOGGING_ENABLED in Settings.

    Write start and stop lines in logs for ease of reading.

    Runs assistant in try block with error logging if it crashes.

    If you manually stop the process, you'll likely trigger an exception here;
    those can be ignored if they are user-created.

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

    """
    With logging set up, let's run the assistant in a try block.
    """

    logging.info('Assistant Started ---------------------------------------')
    try:
        run_assistant()
        logging.info('Assistant Stopped ---------------------------------------')
    except Exception as e:
        logging.error(f'Fatal Error reading from microphone {e}')
        logging.warning('Assistant Crashed ---------------------------------------')