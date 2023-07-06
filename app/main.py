import os 
import filehelper as fh
import logging
import transcribe as t
#import logging.config
#logging.config.fileConfig('/shared/data/')
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='/shared/data/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def setup():
    
    global audioPath
    global textPath
    global dataPath

    audioPath = "/shared/audio/"
    textPath = "/shared/text/"
    dataPath = "/shared/data/"
    #logger = logger.setup_logger(dataPath)
    

    #logging.basicConfig(level=logging.DEBUG)
    #logging.basicConfig(filename=dataPath + 'app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    #logging.debug('This is a debug message')
    #logging.info('This is an info message')
    #logging.warning('This is a warning message')
    #logging.error('This is an error message')
    #logging.critical('This is a critical message')
    
def main():
    try:
        setup()
        
        logging.info("Start")

        for audioFile in (fh.findFilesToProcess(audioPath, dataPath)):
            f = audioFile.split(",")
            t.transcribe_audio_file(audioPath + f[0])
        
        logging.info("End")

            
    except Exception as e:
        print("Main error " + str(e))
    
if __name__ == "__main__":
    main()