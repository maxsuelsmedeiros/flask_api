from flask import Flask
from src.letter_counter import TextCounter
import logging
import os
#confing and adding the logger for debuging and logging purposes

logger : logging.Logger = logging.getLogger(name = __name__)
logger.setLevel(logging.DEBUG)
format : str= '%(asctime)s -> %(levelname)s -> %(module)s -> %(message)s'
formatter : logging.Formatter = logging.Formatter(fmt=format)
stream_handler : logging.StreamHandler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

#adding file handler
try:
    file_handler : logging.FileHandler = logging.FileHandler('logs/api_log.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except FileNotFoundError as e:
    logger.exception(msg='Unable to create the log file,!')
    os.mkdir('logs')
    file_handler : logging.FileHandler = logging.FileHandler('logs/api_log.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except Exception as e:
    logger.error(msg='An unexpected error has ocurred!',exc_info=True)

app : Flask = Flask(__name__)
tc : TextCounter = TextCounter()
@app.route('/')
def main() -> str:
    return 'Welcome to the Text Counter API!'

#adding the character counter

@app.route('/all_char_counter/')
def chars_counter() -> str:
    return str(tc.characters_total_count(''))

if __name__=='__main__':
    main()