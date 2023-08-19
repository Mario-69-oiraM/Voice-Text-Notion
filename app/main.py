import os 
import filehelper as fh
import transcribe as t
import sys
import env.setupenv as envSetup 
import notion
from pathlib import Path
import audiofiles

import logging
envSetup.env_setup()

global logger
logger = logging.getLogger(__name__)
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.environ.get("logfilePath") + 'logfile.log')
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
                
                splitFiles = audiofiles.split_audio(os.environ.get("audioPath") + f, os.environ.get("tempPath"))
                for splitFile in splitFiles:
                    ## Chat GPT 
                    transcribed_text = transcribed_text + " " + t.transcribe_audio_file_openAI(splitFile)

                    #transcribed_text = "[" +  os.path.basename(splitFile) + "]" + transcribed_text + " " + t.transcribe_audio_file_openAI(splitFile)

                text_file = os.environ.get("textPath") + os.path.splitext(f)[0] + '.txt'

                tf = open(text_file, "w")
                logger.info("Saving text " + text_file)
                tf.write(transcribed_text)
                tf.close()
                
                notion.add_page_to_database(Path(text_file).stem, transcribed_text, splitFiles)
                
                os.rename(os.environ.get("audioPath") + f, os.environ.get("processedAudioPath") + f)
                logger.info("Successful transcribe " + f)
            except Exception as e:
                logger.error("transcribe error " + str(e))
                os.rename(os.environ.get("audioPath") + f, os.environ.get("failedPath") + f)
                pass
            
        logging.info("************* End *************")

    except Exception as e:
            logger.error("Main error " + str(e))

    
if __name__ == "__main__":
    main()