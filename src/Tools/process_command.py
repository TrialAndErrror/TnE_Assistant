from src import engine


def cut_trigger_from_command(trigger, command):
    return command.split(f' {trigger} ')[1].lower()


def get_trigger_word_from(command_action):
    trigger_word = command_action.split(' ')[0]
    phrase = command_action.replace(f'{trigger_word} ', '')
    return phrase, trigger_word


def remove_for_from(phrase: str):
    phrase = phrase.strip()
    phrase = phrase[4:] if phrase[:4] == 'for ' else phrase
    phrase = phrase[3:] if phrase[:3] == 'up ' else phrase

    phrase = phrase.strip()
    return phrase
