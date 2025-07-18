# This module reads the all the characters from the text the user sends and respond with the many details, based on the method requested
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
    
    def characters_total_count(self, input_text : str) -> int:
        return 0 