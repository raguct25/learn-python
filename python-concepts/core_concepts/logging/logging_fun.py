# Logging

import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", filename="app.log", filemode="a") # if level is debug the all levels will work
# logging.basicConfig() #if empty logger won't work debug and info level

#format="%(asctime)s %(levelname)s %(message)s old style string formating

def testLogging():
    
    logging.debug("the file has logging debug test")
    logging.info("the file has logging info test")
    logging.warning("the file has logging warning test")
    logging.error("logging error")
    logging.critical("logging critical")


    return "welcome logging"

try:
    # int("test")
    print(testLogging())

except Exception as e:
    # logging.error("logging error")
    print("Exception called", e)