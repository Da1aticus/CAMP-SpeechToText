@echo off
setlocal

:: Check if .venv directory exists
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
    if ERRORLEVEL 1 (
        echo Failed to create virtual environment!
        exit /b 1
    )
    :: Activate the virtual environment
    call .venv\Scripts\activate

    :: Check if requirements.txt exists
    if not exist requirements.txt (
        echo requirements.txt not found!
        exit /b 1
    ) else (
        echo Installing packages from requirements.txt...
        pip install -r requirements.txt
        if ERRORLEVEL 1 (
            echo Failed to install packages!
            exit /b 1
        )
    ) 

) else (
    echo Virtual environment already exists. Skipping creation.
    :: Activate the virtual environment
    call .venv\Scripts\activate
)

echo Virtual environment is ready. Running Whisper server.

:: Navigate to the directory containing WhisperServerMain.py
cd .\src\SpeechToText

:: Run Whisper server
python .\WhisperServerMain.py --c=WhisperServerConfig.yaml

endlocal
