# Trial and Errror Assistant

Trial and Errror Assistant is a voice-activated interface that allows you to quickly and efficiently access the information and media across the web.

If you'd like a video overview of how it works, and how it compares to popular assistants on the market today, check out the "What is Amazon Alexa" video on our YouTube channel here: https://youtu.be/xQJ-3PbJoYY

I also have a more in-depth explanation in the "What is Code" video, where I go over how the main function works in more detail: https://youtu.be/HYN_cM5vYZo

## Special Thanks

Thank you to the following people for helping make this project possible:
* [RajMa](https://pypi.org/user/RajMa/), creator of [PyWhatKit](https://pypi.org/project/pywhatkit/), for providing multiple tools that help enable the Assistant's actions;
* [Natesh M. Bhat](https://pypi.org/user/nateshmbhat/), creator of [Python Text to Speech 3](https://pypi.org/project/pyttsx3/), for providing a simple and clean text-to-speech tool;
* [Anthony Zhang](https://pypi.org/user/Anthony.Zhang/), creator of [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), for providing an easy-to-use voice recognition tool;
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
as long as the user enters the absolute filepath to the script. I included this template because it's a simple way
to integrate with keyboard shortcuts and allow you to quickly bring up Assistant.

NOTE: By default, the Assistant script must be run every time you want to make a new request.
There is no "always-on" functionality on Assistant. I chose this because it is much safer and more secure to have an
assistant that runs when you press a button and tell it to listen, rather than be always listening.

We here at Trial and Errror value your privacy and security and have chosen to sacrifice small measures of functionality 
for large returns in terms of privacy, security, and peace of mind.

# Installation Instructions

1. Download this code to your machine
2. Install required packages to your system
   * PortAudio: sudo apt-get install portaudio19-dev
   * eSpeak: sudo apt-get install espeak
  
3. Create a virtual environment from the requirements.txt
4. Run main.py to start listening for commands


# Help! It doesn't work!
So you downloaded the repository and ran main.py using python3, and it didn't work. Either it flashes on screen,
or it just doesn't show up. That's OK! The joy of open source software is that we can work together on this.

### What should I do?
First, let's make sure that python is able to access all of the libraries and files that it needs.
Start by installing from the requirements.txt (pip3 install -r requirements.txt) and make sure all of those installations
went smoothly.

One common issue comes with installing PyAudio; if you don't have PortAudio installed on your machine, the PyAudio
installation will fail. To resolve it:
* On Ubuntu, you can get it from the package manager:
   * sudo apt-get install portaudio19-dev
    
* On Windows, the steps to install PortAudio are as follows:
    * Download Visual C++ Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/
    * Install the PipWin package in your virtual environment: pip install pipwin
    * Use PipWin to install PyAudio: pipwin install pyaudio
    
* Alternatively, you can manually download and install PortAudio from the PortAudio page: 
  * http://files.portaudio.com/download.html
    
If you are having trouble with espeak, it can also be helpful to install espeak through your package manager or
from the [PyPI page](https://pypi.org/project/python-espeak/) for python espeak.

If those don't work, feel free to reach out to me directly, and we can try and work through the issue! If you share
the issue with me, I can update this readme with more helpful instructions to help solve further issues
