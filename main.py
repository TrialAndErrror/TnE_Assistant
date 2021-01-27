# Tutorial from Programming Hero: https://www.youtube.com/watch?v=AWvsXxDtEkU&t=1267s
from src.Assistant import listen_for_commands, speak
from src.Tools.search import search_web_for
from src import SEARCH_COMMANDS
from src.Tools.youtube import play_youtube_video_for
from src.Tools.process_command import cut_trigger_from_command, get_trigger_word_from
from src.Tools.open import open_page_or_file


def check_for_trigger_command(trigger: str, command: str):
    is_triggered = bool(trigger.lower() in command.lower())
    if is_triggered:
        command_action = cut_trigger_from_command(trigger, command)

        run_command(command_action)
    return is_triggered


def run_command(command_action):
    phrase, trigger_word = get_trigger_word_from(command_action)
    print(f'Phrase was {phrase}\n')
    print(f'Trigger word was {trigger_word}\n')
    if command_action.startswith('play'):
        speak(f'Playing {phrase} on YouTube')
        play_youtube_video_for(phrase)

    elif trigger_word in SEARCH_COMMANDS:
        search_web_for(phrase)
    elif command_action.startswith('open'):
        speak(f'Opening {command_action[5:]}')
        open_page_or_file(phrase)

    else:
        speak(f'The trigger word was {trigger_word}, but I don\'t know what that means.')
        speak(f'I\'ll try to search Google for {phrase}.')
        search_web_for(phrase)


def run_assistant():
    command = listen_for_commands().lower()
    was_assistant_triggered = check_for_trigger_command("google", command)

    if not was_assistant_triggered:
        run_command(command)


if __name__ == '__main__':
    try:
        run_assistant()
    except Exception as e:
        print(f'Fatal Error reading from microphone {e}')


