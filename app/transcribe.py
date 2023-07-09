import speech_recognition as sr
import os
from pydub import AudioSegment

import logging
logger = logging.getLogger(__name__)

# Function to convert to WAV
def convert_to_wav(file, file_type):
    try: 
        logger.debug('convert_to_wav ' + file + ' , ' + file_type)
        wav_file = os.path.splitext(file)[0] + '.wav'
        
        # Load the MP3 file
        if file_type == 'mp3':
            audio = AudioSegment.from_mp3(file)
        elif file_type == 'm4a':
            audio = AudioSegment.from_file(file, format="m4a")
        
        # Export as WAV
        audio.export(wav_file, format='wav')
    except Exception as e: 
        logger.error('convert_to_wav ' + e)

    return(wav_file)

# # Function to convert MP3 to WAV
# def convert_to_wav(mp3_file):
#     wav_file = os.path.splitext(mp3_file)[0] + '.wav'
#     wav = wav_file.split("/")
#     # Load the MP3 file
#     audio = AudioSegment.from_mp3(mp3_file)
#     # Export as WAV
#     audio.export(wav_file, format='wav')
#     return(wav_file)


# # Function to convert M4A to WAV
# def convert_m4a_to_wav(m4a_file):
#     wav_file = os.path.splitext(m4a_file)[0] + '.wav'
#     # Load the M4A file
#     audio = AudioSegment.from_file(m4a_file, format="m4a")
#     # Export as WAV
#     audio.export(wav_file, format="wav")
#     return(wav_file)

# Function to transcribe audio file
def transcribe_audio_file(audio_file):
    
    if audio_file[-3:].upper() == 'MP3':
        audio_file = convert_to_wav(audio_file, 'mp3')
    elif audio_file[-3:].upper() == 'M4A':
        audio_file = convert_to_wav(audio_file,'m4a')
    
    # Initialize the recognizer
    r = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the entire audio file
        audio = r.record(source)

    try:
        # Transcribe the audio
        transcription = r.recognize_google(audio)
        logger.info("Success " + audio_file)
        retun(transcription)

    except sr.UnknownValueError:
        logger.error(" sr.unknownvalueerror: Speech recognition could not understand the audio."  )
    except sr.RequestError as e:
        logger.error("Could not request results from speech recognition service; {0}".format(e))




