#import speech_recognition as sr
import os
#from pydub import AudioSegment
import logging
logger = logging #.getLogger(__name__)

########### Local transcribe 
# Function to convert to WAV
# def convert_to_wav(file, file_type):
#     try: 
#         logger.debug('convert_to_wav ' + file + ' , ' + file_type)

#         wav_file = os.path.splitext(file)[0] + '.wav'
#         wav_file = os.environ.get("wavPath") + os.path.basename(wav_file)
#         # Load the MP3 file
#         if file_type == 'mp3':
#             audio = AudioSegment.from_mp3(file)
#         elif file_type == 'm4a':
#             audio = AudioSegment.from_file(file, format="m4a")
        
#         # Export as WAV
#         audio.export(wav_file, format='wav')
#         logger.debug('Exported file ' + wav_file)

#     except Exception as e: 
#         logger.error('convert_to_wav ' + e)

#     return(wav_file)

# # Function to transcribe audio file
# def transcribe_audio_file_local(audio_file):
    
#     if audio_file[-3:].upper() == 'MP3':
#         audio_file = convert_to_wav(audio_file, 'mp3')
#     elif audio_file[-3:].upper() == 'M4A':
#         audio_file = convert_to_wav(audio_file,'m4a')
    
#     # Initialize the recognizer
#     r = sr.Recognizer()

#     # Load the audio file
#     with sr.AudioFile(audio_file) as source:
#         # Read the entire audio file
#         audio = r.record(source)

#     try:
#         # Transcribe the audio
#         transcription = r.recognize_google(audio)
#         logger.info("Success " + audio_file)
#         return(transcription)

#     except sr.UnknownValueError:
#         logger.error(" sr.unknownvalueerror: Speech recognition could not understand the audio."  )
#         raise
#     except sr.RequestError as e:
#         logger.error("Could not request results from speech recognition service; {0}".format(e))
#         raise

### open transcribe

import requests
import json
import base64
import openai

def transcribe_audio_file_openAI(audio_file):
    try:
        openai.api_key = os.environ.get("openai_api_key")
        logger.debug("transcribe_audio_file_openAI" + audio_file)
        with open(audio_file, "rb") as af:
            transcript = openai.Audio.transcribe(
                file = af,
                model = "whisper-1",
                response_format="text",
                language="en"
            )        
        logger.debug("Success transcribe_audio_file_openAI" + audio_file)
    
        return(transcript)

    except Exception as e:
        logger.error(" Error " + str(e))

