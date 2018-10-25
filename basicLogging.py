import logging

"""

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

"""


def main():
    
    logging.basicConfig(level = logging.DEBUG,filemode='w',filename='output.log',format = '%(asctime)s:%(levelname)s:%(message)s') #more formats online
    
    logging.debug("message")
    
    logging.info("here's a {} variable and an integer {}".format("string",10))
    
if __name__ == "__main__":

    main()
