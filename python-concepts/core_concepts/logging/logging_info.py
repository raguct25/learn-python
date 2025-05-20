# Logging

"""
* Logging is track a program events and debugging 
* It helps for debugging and monitoring and store the run time information
* it can check system health

* If want access , should import logging (native module)
* Config logging (logging.basicConfig())
* if not config the logger won't work debug and info level
* if level give debug the all levels will be works
* if set level error the under error level will be work others won't work
* we can customize string format
* if create log file it won't print in terminal it will update in file

Level of log:

    * Debug
    * Info
    * Warning
    * Error
    * Critical

    - default level log is warning level

Format:

    - string format using %()s, asctime , levelname ,  message
    - asctime - timesatmp
    - levelname - log level name
    - message - user defined message

Filename:

    - we can read logs from file. so can create file. just define filename=FILE_NAME.log extension is .log

Filemode:

    - filemode is how logs add in files accessing mode

    - Append - "a" : append mode create logs and append with existing logs
    - Write - "w" : write mode is overwrites with existing log



"""