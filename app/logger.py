
import logging 

def setup_logger(dataPath):

    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(filename=dataPath + 'app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    return logging.getLogger()



