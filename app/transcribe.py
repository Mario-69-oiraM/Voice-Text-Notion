
#import requests
usr/local/bin/pipimport pip._vendor.requests
import json

def transcribe(audioFile):
    #str(os.getenv('NOTION_TOKEN_heartbeat')) ,                 
    url = "<https://api.openai.com/v1/engines/davinci-codex/completions>"

    audio_file = open(audioFile, "rb").read()

    data = {
        "prompt": f"Please transcribe the following audio file: {audio_file}",
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 1,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + str(os.getenv('GPTKey'))
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    transcription = response.json()["choices"][0]["text"]

    return(transcription)