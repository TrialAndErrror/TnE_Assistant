import logging

from src.Settings import WIKI_SETTINGS, SEARCH_SETTINGS, ASSISTANT_SETTINGS, PLAY_SETTINGS, OPEN_SETTINGS

from src.Actions.Open import open_page_or_file
from src.Actions.Play import play_youtube_video_for
from src.Actions.Search import search_web_for
from src.Actions.Wiki import open_wiki_results_for
from src.Actions.Catchall import do_catchall_action

from src.Tools.process_command import get_first_word_and_phrase_from, listen_for_commands, cut_wake_word_from_command
from src.Tools.wake_triggers import check_for_wake_word


def run_assistant():
    """
    Listen for command;
    Check if wake trigger was detected;

    If so, perform action in command;
    If not, log it and perform action in command anyway.

    :return: None
    """
    command = listen_for_commands().lower()

    """
    Assistant checks the command to see if it has the wake word in it.
    """
    wake_word_detected: bool = check_for_wake_word(command)

    """
    By default, Assistant will check if the wake_word is detected and log the outcome.
    This process happens inside the check_for_wake_word function above.
    """
    if wake_word_detected:
        command_without_wake_word = cut_wake_word_from_command(command)
        perform_action(command_without_wake_word)
    else:
        if ASSISTANT_SETTINGS.get('Require Wake Word', False):
            logging.error(f'Wake Word required by settings; action {command} will not be performed.')
        else:
            """
            Here, the wake word is not required, so it will proceed to perform the action.
            This can be modified in the Settings file.
            """
            logging.info(f'Wake Word not required by settings; continuing to perform action')
            perform_action(command)


def perform_action(command_action):
    """
    Process command and perform the corresponding action.
    This is the core decision-making process behind the Assistant.

    :param command_action: str
    :return: None
    """

    command_word, phrase = get_first_word_and_phrase_from(command_action)
    """
    Get first word and phrase. 
    'phrase' has had helper words removed and whitespace stripped.
    
    Run the determine_command_type function to check through the Settings to see if the command is in a list.
    """
    chosen_action = determine_command_type(command_word)

    if chosen_action == 'play':
        """
        Play using pywhatkit.playonyt()
        """

        logging.debug(f'Recognized {command_word} as Play; playing {phrase}')
        play_youtube_video_for(phrase)

    elif chosen_action == 'wiki':
        """
        Read Wikipedia using wikipedia.summary()
        Open web browser to Wikipedia website
        """
        logging.debug(f'Recognized {command_word} as Wiki; searching Wiki for {phrase}')

        open_wiki_results_for(phrase)

    elif chosen_action == 'search':
        """
        Search on Google using pywhatkit.search()
        """

        logging.debug(f'Recognized {command_word} as Search; searching Google for {phrase}')
        search_web_for(phrase)

    elif chosen_action == 'open':
        """
        Open various locations;
        currently limited to e-mail only based on url in Settings
        """

        logging.info(f'Recognized {command_word} as open; attempting to open {phrase[5:]}')
        open_page_or_file(phrase)

    else:
        """
        Catchall Option:
        When the first word is not recognized, Assistant goes here.
        Currently set to Google Search by default.
        """
        logging.info(f'Failed to recognize {command_word} (which is set to catchall by default); reverting to search')

        """
        Below is the catchall action to do when the command is not recognized.
        By default, it is set to search the web for the phrase.
        """
        do_catchall_action(phrase, command_word)


def determine_command_type(command_word):
    """
    Check Settings to get the list of available commands (or default to these lists if no settings found).

    By default, the
    :param command_word:
    :return:
    """
    default_play_commands = ['play']
    default_wiki_commands = ['wiki', 'what', 'who']
    default_search_commands = ['search', 'find', 'google']
    default_open_commands = ['open']

    chosen_action = 'catchall'

    actions_list = [
        PLAY_SETTINGS.get('Commands', default_play_commands),
        WIKI_SETTINGS.get('Commands', default_wiki_commands),
        SEARCH_SETTINGS.get('Commands', default_search_commands),
        OPEN_SETTINGS.get('Commands', default_open_commands)]

    """
    Actions list is a list of all of the options of command words that can trigger that particular action.
    
    Iterate over the list of actions until you find a word that matches; 
    then set the chosen action to the first action in that list to return as the chosen action.
    
    If the command matches nothing, it will stay as 'catchall' by default.
    """
    for command_list in actions_list:
        if command_word in command_list:
            chosen_action = command_list[0]
            break

    return chosen_action
