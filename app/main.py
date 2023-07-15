import os 
import filehelper as fh
import transcribe as t
import logging
import sys
import env.setupenv as envSetup 
import notion


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
    
    global audioPath
    global textPath
    global dataPath

    envSetup.env_setup()

def main():
    try:
        setup()
        notion.create_page()
        for f in (fh.fileInDirectory()):
            #f = audioFile.split(",")
            try: 
                logger.info("Transcribing " + f)
                ## local 
                ##transcribed_text = t.transcribe_audio_file_local(os.environ.get("audioPath") + f)
                
                ## Chat GPT 
                transcribed_text = t.transcribe_audio_file_openAI(os.environ.get("audioPath") + f)

                text_file = os.environ.get("textPath") + os.path.splitext(f)[0] + '.txt'
                tf = open(text_file, "w")
                logger.info("Saving text " + text_file)
                tf.write(transcribed_text)
                tf.close()

                logger.info("Successful transcribe " + f)
                os.rename(os.environ.get("audioPath") + f, os.environ.get("processedAudioPath") + f)

            except Exception as e:
                logger.error("transcribe error " + str(e))
                pass
            
        logging.info("************* End *************")

    except Exception as e:
            logger.info("Main error " + str(e))
    
if __name__ == "__main__":
    main()