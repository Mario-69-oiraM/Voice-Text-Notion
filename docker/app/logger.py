
import logging 

def setup_logger():

    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(filename='/shared/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    return logging.getLogger()



