#!/usr/bin/env python3

import logging
import sys

import sublog

logger = logging.getLogger()

# http://stackoverflow.com/a/24956305/1076493
# filter messages lower than level (exclusive)
class MaxLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno < self.level

def main():
    # redirect messages to either stdout or stderr based on loglevel
    # stdout < logging.WARNING <= stderr
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(module)s]: %(message)s')
    logging_out = logging.StreamHandler(sys.stdout)
    logging_err = logging.StreamHandler(sys.stderr)
    logging_out.setFormatter(formatter)
    logging_err.setFormatter(formatter)
    logging_out.addFilter(MaxLevelFilter(logging.WARNING))
    logging_out.setLevel(logging.DEBUG)
    logging_err.setLevel(logging.WARNING)

    # root logger, no __name__ as in submodules further down the hierarchy
    global logger
    logger.addHandler(logging_out)
    logger.addHandler(logging_err)
    logger.setLevel(logging.DEBUG)

    logger.info("An INFO message from " + __name__)
    logger.error("An ERROR message from " + __name__)
    sublog.log()

    sys.exit(1)

if __name__ == '__main__':
    main()
