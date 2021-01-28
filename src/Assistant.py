import logging

from src.Actions.Open import open_page_or_file
from src.Actions.Play import play_youtube_video_for
from src.Actions.Search import search_web_for
from src.Actions.Wiki import open_wiki_results_for
from src.Settings import print_custom_intro, WIKI_SETTINGS, SEARCH_COMMANDS
from src.Tools.process_command import get_first_word_and_phrase_from, listen_for_commands
from src.Tools.wake_triggers import check_for_trigger_command, set_trigger_command
from src.Actions.Catchall import do_catchall_action
from src.Tools.process_command import cut_trigger_from_command


def run_assistant():
    """
    Listen for command;
    Check if wake trigger was detected;

    If so, perform action in command;
    If not, log it and perform action in command anyway.

    :return: None
    """
    command = listen_for_commands().lower()
    print_custom_intro()

    """
    set_trigger_command is a function in the user file which allows you to set a keyword to trigger the assistant.
    """
    trigger_command = set_trigger_command()
    is_triggered = check_for_trigger_command(trigger_command, command)

    if is_triggered:
        command_without_trigger = cut_trigger_from_command(trigger_command, command)
        perform_action(command_without_trigger)
    else:
        perform_action(command)


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
        open_wiki_results_for(phrase)

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
