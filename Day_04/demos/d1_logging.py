"""
Demo logging

Levels: login.critical, login.warning, etc...
- critical
- error
- warning
- info
- debug

-> Use 'logging' module, include timestamp and log level, write short and clear msg, config for multiple use cases
"""

import logging
from time import asctime

# Always create a config for logging -> print the type of error in level=
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s", # -8s : 8 characters spaces
    filename="logging_demo.log",
    filemode="a" # a for append, w for write (overwrite)

)

logging.warning("This program is for demo purposes only")
# logging.error("There is an error")

def main():
    logging.info("Starting the program")
    retrieve_data()
    store_data()
    logging.info("Ending the program")

def retrieve_data():
    logging.info("Downloading data")
    # do stuff
    data = [1, 2, 3]
    logging.debug(data)


def store_data():
    logging.info("Storing data")
    # do stuff


if __name__ == '__main__':
    main()
