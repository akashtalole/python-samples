from time import time
from contextlib import contextmanager

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"


@contextmanager
def new_log_file(name):    
    try:
        logname = name
        f = open(logname, 'w')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print "logfile created"
        f.close()


