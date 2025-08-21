# This module reads the all the characters from the text the user sends and respond with the many details, based on the method requested
# add a Levenshtein distance method
import logging

class TextCounter:

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
    #return the number of charachters of a input
    def characters_total_count(self, input_text : str) -> dict[str,int]:
        counter : dict = dict()
        input_text_without_spaces : str = input_text.replace(' ', '')
        for letter in input_text_without_spaces:
            counter[letter] = counter.get(letter,0) + 1
        return counter