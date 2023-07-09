import os 
import filehelper as fh
import transcribe as t
import logging
import sys

global logger
logger = logging.getLogger(__name__)
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(module)s : %(message)s')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('started main')

 
def setup():
    
    global audioPath
    global textPath
    global dataPath

    audioPath = "/shared/audio/"
    textPath = "/shared/text/"
    dataPath = "/shared/data/"
    processedAudioPath = "/shared/audio/processed/"
    
def main():
    try:
        setup()
        for audioFile in (fh.fileInDirectory(audioPath)):
            f = audioFile.split(",")
            try: 
                print(t.transcribe_audio_file(audioPath + f[0]))
                logger.info("Successful transcribe " + audioPath + f[0])

            except ex as e:
                logger.error("transcribe error " + str(e))
            
        logging.info("End")

    except Exception as e:
            logger.info("Main error " + str(e))
    
if __name__ == "__main__":
    main()