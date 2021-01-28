DEBUG_LOGGING_ENABLED = True

WIKI_SETTINGS = {
    'Commands':
        [
            'what',
            'who',
            'wiki',
            'wikipedia'
        ],
    'Lines to Read': 1
}
SEARCH_COMMANDS = [
    'look',
    'lookup',
    'find',
    'search',
    'google'
]
ASSISTANT_SETTINGS = {
    'Wake Word': None
}


def set_mail_url():
    mail_url = 'https://mail.google.com/mail/u/0/'
    return mail_url


def print_custom_intro():
    print('Welcome to Ratty\'s Assistant\n'
          '\n'
          '\n'
          'You can ask me to play or look up anything!\n'
          '\n'
          'You can Say:\n'
          '\tSearch for Airline tickets to Florida\n'
          '\tPlay Miley Cyrus - Born in the USA\n'
          '\tWhat is Coronavirus?\n'
          '\tLookup Medical Insurance Prices\n'
          '\tPlay Anthony Fauci Speeches 2020\n'
          '\n'
          '\n'
          'Listening for commands...\n'
          '\n')