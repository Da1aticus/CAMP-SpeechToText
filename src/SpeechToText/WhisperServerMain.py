# Python packages
import os
import sys
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
sys.path.insert(0, projectRoot) # Set projectRoot as the working directory
import yaml
import click
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import shutil
from faster_whisper import WhisperModel

# Custom packages
from Common.CommonFunctions import ParseConfiguration

# Server function
def WhisperServer(config):

    # init whisper
    model = WhisperModel(model_size_or_path=config["whisper"]["model"], 
                         device=config["whisper"]["device"], 
                         compute_type=config["whisper"]["computeType"])

    # init fast api server
    serverApp = FastAPI()
    
    # handle requests
    @serverApp.post("/whisper")
    def HandleAudioFiles(file: UploadFile = File(...)):
              
        try:
            # receive audio file from client
            with open(f"audioSample.wav", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # transribe audio file
            segments, _ = model.transcribe(audio="audioSample.wav", 
                                           language="en", 
                                           condition_on_previous_text=False,
                                           no_speech_threshold=config["whisper"]["noSpeechThreshold"])
            segments = list(segments)
                        
            transcription = ""
            for segment in segments:
                transcription += segment.text              
                           
            return JSONResponse(content={"transcription": transcription}, status_code=200)
        
        except Exception as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)    
        
    uvicorn.run(serverApp, host=config["server"]["host"], port=config["server"]["port"])
    
# main function
@click.command()
@click.option('--c', help="YAML configuration file")
def main(c):
    
    config = ParseConfiguration(c)
    WhisperServer(config)   

# main
if __name__ == "__main__":
    main()
 