#import openai
import speech_recognition as sr
import os

# Set up your OpenAI API credentials
#openai.api_key = str(os.getenv('GPTKey'))

# Function to convert MP3 audio to WAV format
def convert_to_wav(mp3_file):
    wav_file = os.path.splitext(mp3_file)[0] + '.wav'
    os.system(f'ffmpeg -i {mp3_file} {wav_file}')
    return wav_file

# Function to transcribe audio file using speech recognition
def transcribe_audio_file(audio_file :str):
    # Initialize the recognizer
    r = sr.Recognizer()
    
    print(audio_file[-3:].upper())
    if audio_file[-3:].upper() == 'MP3':
        audio_file = convert_to_wav(audio_file)
        
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the entire audio file
        audio = r.record(source)

    try:
        # Transcribe the audio using the whispering language model
        transcription = r.recognize_sphinx(audio, language='whisper')

        # Return the transcription
        return transcription

    except sr.UnknownValueError:
        print("Whispering not recognized.")
        return None

# Function to generate a response from ChatGPT
# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=prompt,
#         max_tokens=100,
#         temperature=0.7,
#         n=1,
#         stop=None,
#         timeout=15,
#     )

#     if 'choices' in response and len(response.choices) > 0:
#         return response.choices[0].text.strip()
#     else:
#         return None

# Provide the path to your MP3 audio file
#mp3_file_path = "path/to/your/audio_file.mp3"

# Convert the MP3 audio file to WAV format
#wav_file_path = convert_to_wav(mp3_file_path)

# Transcribe the audio file
#transcription = transcribe_audio_file(wav_file_path)

# if transcription:
#     # Provide the transcription as the prompt for ChatGPT
#     prompt = "You: " + transcription

#     # Generate a response from ChatGPT based on the transcription
#     response = generate_response(prompt)

#     # Print the response
#     print("ChatGPT:", response)

# # Remove the temporary WAV file
# os.remove(wav_file_path)
