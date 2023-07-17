import os 
import filehelper as fh
import transcribe as t
import logging
import sys
import env.setupenv as envSetup 
import notion
from pathlib import Path
import audiofiles
import audiofiles

global logger
logger = logging.getLogger(__name__)
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s : %(message)s')

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('************* Started main *************')
 
def setup():
    
    #global audioPath
    #global textPath
    #global dataPath

    envSetup.env_setup()

def main():
    try:
        setup()
        for f in (fh.fileInDirectory()):
            #f = audioFile.split(",")
            try: 
                transcribed_text = ""
                logger.info("Transcribing " + f)
                splitFiles = ""
                ## local 
                ##transcribed_text = t.transcribe_audio_file_local(os.environ.get("audioPath") + f)
    
                #transcribed_text = t.transcribe_audio_file_openAI(os.environ.get("audioPath") + f)

                splitFiles = audiofiles.split_audio(os.environ.get("audioPath") + f, os.environ.get("tempPath"))
                for splitFile in splitFiles:
                    ## Chat GPT 
                    transcribed_text = transcribed_text + " " + t.transcribe_audio_file_openAI(splitFile)

                text_file = os.environ.get("textPath") + os.path.splitext(f)[0] + '.txt'

                tf = open(text_file, "w")
                logger.info("Saving text " + text_file)
                tf.write(transcribed_text)
                tf.close()
                
                notion.add_page_to_database(Path(text_file).stem, transcribed_text)
                
                os.rename(os.environ.get("audioPath") + f, os.environ.get("processedAudioPath") + f)
                logger.info("Successful transcribe " + f)
            except Exception as e:
                logger.error("transcribe error " + str(e))
                os.rename(os.environ.get("audioPath") + f, os.environ.get("failedPath") + f)
                pass
            
        logging.info("************* End *************")

    except Exception as e:
            logger.info("Main error " + str(e))

    
if __name__ == "__main__":
    main()