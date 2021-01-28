# Trial and Errror Assistant

Trial and Errror Assistant is a voice-activated interface that allows you to quickly and efficiently access the information and media across the web.

## Special Thanks

Thank you to the following people for helping make this project possible:
* [RajMa](https://pypi.org/user/RajMa/), creator of [PyWhatKit](https://pypi.org/project/pywhatkit/), for providing multiple tools that help enable the Assistant's actions;
* [Natesh M. Bhat](https://pypi.org/user/nateshmbhat/), creator of [Python Text to Speech 3](https://pypi.org/project/pyttsx3/), for providing a simple and clean text-to-speech tool;
* [Anthony Zhang](https://pypi.org/user/Anthony.Zhang/), creator of [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), for providing an easy to use voice recognition tool;
* and [Programming Hero](https://www.youtube.com/channel/UCStj-ORBZ7TGK1FwtGAUgbQ), for the comprehensive and entertaining [video tutorial](https://www.youtube.com/watch?v=AWvsXxDtEkU) on how to make the underlying libraries work together. If you're interested in this Assistant and how to develop your own, I highly recommend starting with his video to get a great overview of the process!

## Usage

Run 'main.py' using python3 to start the Assistant. 
Assistant will automatically start listening for a command.

## Commands Currently Supported:

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

### Open File
This section is currently under development. Eventually, it will have filesystem integrations and more.
For now, you can use it to open your web browser to your e-mail to quickly check for new messages.
* "open mail"
* "send mail"
* "open messages"
* "send e-mail"


## Customization
Assistant was built around making your life easier and simplifying common tasks. In order to achieve that goal,
the Settings.py file in src can be modified to your liking. You will see lists of commands for each of the actions
listed above, as well as some other miscellaneous settings. Feel free to modify the settings in that file with your
own preferred wake words or keywords. Additionally, by default, the Assistant is setup to try and run your commands
even when a wake word is not detected. This functionality can be disabled in the Settings file.


### Shortcut
Along the lines of customization, there is a template bash file called 'assistant.sh' included in src/bash/.
This script can be run in a bash terminal to start the assistant directly, 
as long as the user enters the absolute filepath to the script. I included this template because it's a quick way
to integrate with keyboard shortcuts and allow you to quickly bring up Assistant.

NOTE: By default, the Assistant script must be run every time you want to make a new request.
There is no "always-on" functionality on Assistant. I chose this because I personally do not need a device that
is always listening to me, and I'd much rather have one where I can press a button and tell it to listen.
There are simple workarounds to make this Assistant work as an always-on listening device, we here at Trial and Errror
value your privacy and security and will gladly sacrifice small measures of functionality for large returns in terms of 
privacy, security, and peace of mind.