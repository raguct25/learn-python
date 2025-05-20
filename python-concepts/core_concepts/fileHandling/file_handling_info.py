# Filehandling

"""
* StringIo, CSV module, Open, Filemode, Write, with
* Filehandling is essential part of working with data in python

* we can mainpulate file opertions read, write, read line by line, check existing files

StringIO:

    - its use for without physical file acessing. string like as file
    - in-built moudle and it from IO module

Write:

    - file.write("FILE CONTENT")
    

Open:

    - open(FILE_PATH, FILE_MODE)
    - when open the file we should close the file
    - if not file exist ("w") write mode is create file and it' overwrite contents
    - if not file exist ("a") append mode is create file and it' not overwrite contents

With statement:

    - it clear to open objects and safe close automatically
    - normal declartion open method is not close automatically we will trigger. if occur any error the open not closed 
    - if not close properly. it can croupt
    - alternatively we can use try and finally
    - with manage automatically so it create __enter__ and __exit__ objects (db connections, websockets, any network connections)
    - first call in context manager, __enter__ will executed and return file object
    - second call __exit__ (exception hnadling don't consider it automatically closed)

"""