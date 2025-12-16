from Terminal import clear_terminal
# In logging we have 5 security levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
#In logging, if a info message is sent but the security level is higher than this, the message wont be seen
import logging

logging.info("You have 20 mails in your inbox!") #displays root because its using the default logger
logging.critical("All components failed!")
#python has a default security level of warning so info was not shown
logging.warning("You have 20 mails in your inbox!")
clear_terminal()
#to change to security level:
logging.basicConfig(level=logging.DEBUG, force=True) #force=True tells python to ignore previous logging level
logging.info("You have 20 mails ")
logging.critical("All components failed!")
#This was logging with the default logger and its settings. Now lets make our own logger:
clear_terminal()

logger = logging.getLogger("Robert Logger") #stating the name used each time
logger.info("The best logger was just created!")
logger.critical("Your computer is going to explode!!!")
logger.log(logging.ERROR, "An error occured!")  #this is an alternative way of stating the level of the message
clear_terminal()
# This isnt what we really want. A much better way to display all the errors, messages, etc is to put them in a log file:
#for this we must create a file handler:
logger.setLevel(logging.DEBUG)  #sets the logger level

handler = logging.FileHandler("mylog.log")#file name
handler.setLevel(logging.INFO) #sets handler level

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s") #How the file will be structured
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug("This is a debug message")
logger.info("This is important information")
#the file only has the Info message because its level is set to logging
#The message also lacks structure. We dont know its security level or What logger sent it. To fix this, we can make a formater(L35):
