#Logs are messages your program writes to record events, errors, warnings, or informational messages.
#They are useful for debugging, monitoring, and keeping a history of what happened in your program.

import logging #Python module for logging messages to files or console.
import os  #Provides functions to interact with the operating system (paths, directories, etc.).
from datetime import datetime

#log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# datetime.now() → gets the current date and time.
# .strftime('%m_%d_%Y_%H_%M_%S') → formats the timestamp as month_day_year_hour_minute_second, e.g., 08_30_2025_15_40_12.
# f".... .log" → adds the .log extension.

#logs directory
logs_path = os.path.join(os.getcwd(),"logs") #combines the current directory with "logs", creating a path for a folder called logs inside your project
# getcwd -->gets the current working directory of your project.
os.makedirs(logs_path,exist_ok=True) #creates directories recursively if they don’t exist. 
#exist_ok=True --> prevents an error if the directory already exists.

#full log file path
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) #combines the folder path (logs_path) with the file name, creating the 
#full path to the log file, e.g.,

logging.basicConfig(
    filename=LOG_FILE_PATH, #tells Python to write log messages to this file.
    format = "%(asctime)s - %(levelname)s - %(message)s", #defines the log message format:
    level=logging.INFO #ou are telling Python: “Only log messages that are INFO level or higher --> General information about error.”
)


#whenever we get an exception , take that exception , logging into the logger file and use log.info to put it into the file

# try: block
# Yahan code run hota hai jo error de sakta hai.
# Agar koi error nahi hoti → normal execution.

# except Exception as e:
# Agar error ho jaye → ye block execute hota hai.
# e mein error ka detail store hota hai, jaise “division by zero”.

# logging.info(f"Exception aayi: {e}")
# logging.info() file mein ek message likhne ke liye use hota hai.
# Ye message file mein date/time ke saath store ho jata hai.
# Is tarah, aap future mein dekh sakte ho ki kab aur kaun si error aayi thi.

#jb bhi kisi file mein log crerate krne hain to logging ko import krna hai
# from src.logger import logging