from flask import Flask
from src.letter_counter import TextCounter

app : Flask = Flask(__name__)
tc : TextCounter = TextCounter()
@app.route('/')
def main():
    return 'Welcome to the Text Counter API!'

if __name__=='__main__':
    main()