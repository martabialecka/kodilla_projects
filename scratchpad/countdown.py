import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="dupka.log")

def countdown (n):
    if n==0:
        return
    print (n)
    countdown (n-1)

#if __name__ == "__main__":
    #logging.debug("The program was called with this parameters %s" % sys.argv[1])
    #logging.debug("First parameter is %s" % sys.argv[1])

countdown (99)
print ("mamaigoniko")
