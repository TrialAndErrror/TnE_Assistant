

def cut_trigger_from_command(trigger, command):
    """
    Removes trigger from command using string split on the command string.

    Converts command to lowercase.

    Returns the rest of the command string after removing the trigger.

    :param trigger: str
    :param command: str
    :return: str
    """
    return command.split(f' {trigger} ')[1].lower()


def get_first_word_from(command_action):
    """
    Split command action on spaces;
    sets trigger word to first word in list;
    removes trigger word from command action and sets as phrase.

    :param command_action: str
    :return: phrase: str; trigger_word: str
    """
    trigger_word = command_action.split(' ')[0]
    phrase = command_action.replace(f'{trigger_word} ', '')
    return phrase, trigger_word


def remove_helper_words(phrase: str):
    """
    Remove 'for' and 'up' from the beginning of param phrase.
    Removes whitespace before and after removing words.

    Returns cleaned phrase.
    :param phrase: str
    :return: phrase: str
    """

    phrase = phrase.strip()
    phrase = phrase[4:] if phrase[:4] == 'for ' else phrase
    phrase = phrase[3:] if phrase[:3] == 'up ' else phrase
    phrase = phrase.strip()
    return phrase
