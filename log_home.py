import logging
from random import randint
import datetime
logging.basicConfig(format='%(asctime)s--%(message)s:%(levelname)s', filename="log_file.log", level = logging.DEBUG)
for i in range(10):
    number  = randint(0,50)
    if number <= 9:
        logging.debug("This number causes debug")
    elif number <= 19:
        logging.info("This number causes info")
    elif number <= 29:
        logging.info("This number causes warning")
    elif number <= 39:
        logging.info("This number causes error")
    elif number <= 50:
        logging.info("This number causes critical")



