# Trial and Errror Assistant

Trial and Errror Assistant is a voice-activated interface that allows you to quickly and efficiently access the information and media across the web.

## Special Thanks

Thank you to the following people for helping make this project possible:
* [RajMa](https://pypi.org/user/RajMa/), creator of [PyWhatKit](https://pypi.org/project/pywhatkit/), for providing multiple tools that help enable the Assistant's actions;
* [Natesh M. Bhat](https://pypi.org/user/nateshmbhat/), creator of [Python Text to Speech 3](https://pypi.org/project/pyttsx3/), for providing a simple and clean text-to-speech tool;
* [Anthony Zhang](https://pypi.org/user/Anthony.Zhang/), creator of [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), for providing an easy to use voice recognition tool;
* and [Programming Hero](https://www.youtube.com/channel/UCStj-ORBZ7TGK1FwtGAUgbQ), for the comprehensive and entertaining [video tutorial](https://www.youtube.com/watch?v=AWvsXxDtEkU) on how to make the underlying libraries work together. If you're interested in this Assistant and how to develop your own, I highly recommend starting with his video to get a great overview of the process!

## Usage

Run 'main.py' to start the Assistant. Assistant will automatically start listening for a command.

Commands Currently Supported:

### Play on Youtube
These commands will bring up a video for you to watch on YouTube in your web browser.

* "play classical music"
* "see 7 wonders of the world"
* "hear bluejays calling"
* "watch basketball highlights"
* "visit madrid in the springtime"
* "listen to famous american speeches"
  
### Search on Google
These commands will search Google for the information you requested.
* "look up flights to Antarctica"
* "find blue suede shoes"
* "search best pizza place in kentucky"
* "google how to repair a cracked screen"
* "find where Albert Einstein went to college"


### Search on Wikipedia
These commands will search Wikipedia for the person, place, or thing you want to learn more about. Great for 20 questions!
* "what is Prussia"
* "who was Napoleon"
* "wikipedia Nudibranch"
* "who are the Beatles"
* "find where Albert Einstein went to college"

## Shortcut

Included in src/bash/ is a file called 'assistant.sh', which can be run in a bash terminal to start the assistant directly. I included this file for convenience so that you can reference an easy way to run the script or map it to a keyboard shortcut. If you wish to use this, replace the directories included with the python and file directories on your system.
