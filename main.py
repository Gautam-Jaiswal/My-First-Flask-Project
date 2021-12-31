from flask import Flask
import random

num = random.randint(0,9)
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>GUESS A NUMBER BETWEEN 0 AND 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def guess(number):
    if number > num:
        return '<h1>GUESS IS TOO HIGH</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < num:
        return '<h1>GUESS NUMBER IS TOO LOW</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1>CORRECT ANSWER !!!! </h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == '__main__':
    app.run(debug=True)