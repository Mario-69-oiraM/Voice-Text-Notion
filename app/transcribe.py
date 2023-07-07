import openai
#import speech_recognition as sr
import os
from pocketsphinx import AudioFile, get_model_path

#from pydub import AudioSegment

# Set up your OpenAI API credentials
#openai.api_key = str(os.getenv('GPTKey'))


model_path = get_model_path()

def transcribe_audio_file(audio_file):
    
    if audio_file[-3:].upper() == 'MP3':
        audio_file = convert_to_wav(audio_file)

    config = {
        'verbose': False,
        'audio_file': '" + audio_file + " ',
        'hmm': get_model_path('en-us'),
        'lm': get_model_path('en-us.lm.bin'),
        'dict': get_model_path('cmudict-en-us.dict')
    }

    audio = AudioFile(**config)
    for phrase in audio:
        print(phrase)
    

# Function to convert audio to WAV format
def convert_to_wav(audio_file):
    wav_file = os.path.splitext(audio_file)[0] + '.wav'
    #os.system(f'ffmpeg -i {audio_file} {wav_file}')
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(audio_file)
    sound.export(wav_file, format="wav")
    
    return wav_file

# Function to transcribe audio file using speech recognition
# def transcribe_audio_file(audio_file):

#     if audio_file[-3:].upper() == 'MP3':
#         audio_file = convert_to_wav(audio_file)

#     # Initialize the recognizer
#     r = sr.Recognizer()

#     # Load the audio file
#     with sr.AudioFile(audio_file) as source:
#         # Read the entire audio file
#         audio = r.record(source)

#     try:
#         # Transcribe the audio using the whispering language model
#         transcription = r.recognize_sphinx(audio, language='whisper')

#         # Return the transcription
#         return transcription

#     except sr.UnknownValueError:
#         print("Whispering not recognized.")
#         return None

# Function to generate a response from ChatGPT
# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=prompt,
#         max_tokens=2000,
#         temperature=0,
#         n=1,
#         stop=None,
#         timeout=15,
#     )

#     if 'choices' in response and len(response.choices) > 0:
#         return response.choices[0].text.strip()
#     else:
#         return None

# # Provide the path to your audio file
# audio_file_path = "path/to/your/audio_file.mp3"

# # Convert the audio file to WAV format
# wav_file_path = convert_to_wav(audio_file_path)

# # Transcribe the audio file
# transcription = transcribe_audio_file(wav_file_path)

# if transcription:
#     # Provide the transcription as the prompt for ChatGPT
#     prompt = "You: " + transcription

#     # Generate a response from ChatGPT based on the transcription
#     response = generate_response(prompt)

#     # Print the response
#     print("ChatGPT:", response)

# # Remove the temporary WAV file
# os.remove(wav_file_path)
