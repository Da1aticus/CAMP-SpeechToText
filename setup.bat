@echo off
:: Check if requi::ents.txt exists
if not exist requi::ents.txt (
    echo requi::ents.txt not found!
    exit /b 1
)

:: Create a virtual environment named .venv
python -m venv .venv

:: Check if venv creation was successful
if ERRORLEVEL 1 (
    echo Failed to create virtual environment!
    exit /b 1
)

:: Activate the virtual environment
call .venv\Scripts\activate

:: Check if activation was successful
if "%VIRTUAL_ENV%" == "" (
    echo Failed to activate virtual environment!
    exit /b 1
)

:: Install packages from requirements.txt
pip install -r requirements.txt

:: Check if installation was successful
if ERRORLEVEL 1 (
    echo Failed to install packages!
    exit /b 1
)

echo Virtual environment setup complete and packages installed successfully. Running Whisper server.

:: Run Whisper server
python .\src\SpeechToText\WhisperServerMain.py --c=WhisperServerConfig.yaml

exit /b 0
