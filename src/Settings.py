import subprocess

DEBUG_LOGGING_ENABLED = True

OPEN_COMMANDS = [
    'open',
    'send'
]

EMAIL_COMMANDS = [
    'mail',
    'email',
    'e-mail',
    'message',
    'messages'
]

OPEN_SETTINGS = {
    'Commands': OPEN_COMMANDS,
    'Mail URL': 'https://mail.google.com/mail/u/0/',
    'Email': EMAIL_COMMANDS
}

PLAY_COMMANDS = [
    'play',
    'watch',
    'hear',
    'listen',
    'see',
    'visit'
]

PLAY_SETTINGS = {
    'Commands': PLAY_COMMANDS,
}

WIKI_COMMANDS = [
    'what',
    'who',
    'wiki',
    'wikipedia'
]

WIKI_SETTINGS = {
    'Commands': WIKI_COMMANDS,
    'Lines to Read': 1
}

SEARCH_COMMANDS = [
    'search',
    'look',
    'lookup',
    'find',
    'google'
]
SEARCH_SETTINGS = {
    'Commands': SEARCH_COMMANDS
}

ASSISTANT_SETTINGS = {
    'Wake Word': 'Assistant',
    'Require Wake Word': False
}


def print_custom_intro():
    """
    Clear Screen and display introductory text.
    :return: None
    """

    subprocess.call('clear', shell=True)

    print('Welcome to Ratty\'s Assistant\n'
          '\n'
          '\n'
          'You can ask me to play or look up anything!\n'
          '\n'
          'You can Say:\n'
          '\tSearch Maps of Ancient Rome\n'
          '\tPlay Miley Cyrus - Born in the USA\n'
          '\tWho is Al Gore?\n'
          '\tFind Car Rentals Near Me\n'
          '\tPlay Chocolate Chip Cookie Recipe No Eggs'
          '\n'
          '\n'
          'Listening for commands...\n'
          '\n')
