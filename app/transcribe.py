#import speech_recognition as sr
import os
import logging
logger = logging #.getLogger(__name__)
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

