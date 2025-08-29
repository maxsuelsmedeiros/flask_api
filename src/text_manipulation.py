# This module reads the all the characters from the text the user sends and respond with the many details, based on the method requested
# add a Levenshtein distance method
import logging
import re
import unicodedata

class TextManipulator:

    logger: logging.Logger

    def __init__(self) -> None:
        self.logger : logging.Logger = logging.getLogger(name = __name__)
        self.logger.setLevel(logging.DEBUG)
        format : str= '%(asctime)s -> %(levelname)s -> %(module)s -> %(message)s'
        formatter : logging.Formatter = logging.Formatter(fmt=format)
        stream_handler : logging.StreamHandler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        return

    def __repr__(self) -> str:
        self.logger.debug(msg='Returning class representation.')
        return 'TextCounter'
    
    #remove special characters from a input
    def remove_special_characters(self, input_text: str) -> str:
        normalizedtext = unicodedata.normalize('NFD', input_text)
        # Remove acentos
        no_accents = ''.join(
            c for c in normalizedtext if unicodedata.category(c) != 'Mn'
        )
        # Remove caracteres especiais, mantendo letras, números e espaços
        cleanString = re.sub(r'[^A-Za-z0-9 ]+', '', no_accents)
        return cleanString
    #return the number of charachters of a input
    def characters_total_count(self, input_text : str) -> dict[str,int]:
        counter : dict = dict()
        input_text_without_spaces : str = input_text.replace(' ', '')
        for letter in input_text_without_spaces:
            counter[letter] = counter.get(letter,0) + 1
        return counter