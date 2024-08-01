# CAMP-SpeechToText
This is a Speech to Text server that is a part of [CAMP-Conversation Assistant for Miscommunication prevention](https://github.com/MHudomalj/CAMP) application. It is based on [FastAPI](https://github.com/fastapi/fastapi) and [faster-whisper](https://github.com/SYSTRAN/faster-whisper) libraries. 

The server was only tested on Windows PC. To run it, double click on [setup.bat](https://github.com/Da1aticus/CAMP-SpeechToText/blob/main/setup.bat) file. The first time that the script is ran, it will create a Pyhon virtual environment, install all needed packages located in [requirements.txt](https://github.com/Da1aticus/CAMP-SpeechToText/blob/main/requirements.txt) and start a text to speech server. Any subsequent time, the script only starts the server. 

The user can modify server or speech-to-text settings in [YAML configuration file](https://github.com/Da1aticus/CAMP-SpeechToText/blob/main/src/SpeechToText/WhisperServerConfig.yaml).
