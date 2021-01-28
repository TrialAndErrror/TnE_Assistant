# Trial and Errror Assistant

Trial and Errror Assistant is a digital assistant that can help with accessing quick information on the internet.

## Special Thanks

Special Thanks to the following people:
* [RajMa](https://pypi.org/user/RajMa/), creator of [PyWhatKit](https://pypi.org/project/pywhatkit/), which makes most of this project possible;
* [Natesh M. Bhat](https://pypi.org/user/nateshmbhat/), creator of [Python Text to Speech 3](https://pypi.org/project/pyttsx3/), which enables the Assistant to read text aloud;
* [Anthony Zhang](https://pypi.org/user/Anthony.Zhang/), creator of [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), which helps Assistant to recognize the commands you give it;
* and [Programming Hero](https://www.youtube.com/channel/UCStj-ORBZ7TGK1FwtGAUgbQ), for the wonderful [video tutorial](https://www.youtube.com/watch?v=AWvsXxDtEkU) on how to make the underlying libraries work together.

## Usage

Run 'main.py' and follow the prompts in the console to make a request to the Assistant.

For Example:
* "play classical music" will search YouTube for Classical Music and open a relevant result in your web browser.
* "search water bottles" will search Google for water bottles and open the search page in your browser.
* "open mail" will open your web browser to Gmail
* "who is napoleon" will search Wikipedia for Napoleon

## Shortcut

Included in src/bash/ is a file called 'assistant.sh', which can be run in a bash terminal to start the assistant directly. I included this file for convenience so that you can reference an easy way to run the script or map it to a keyboard shortcut. If you wish to use this, replace the directories included with the python and file directories on your system.
