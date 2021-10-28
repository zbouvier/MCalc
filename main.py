from flask import Flask, render_template
from util import calcScore, KEYS
app = Flask(__name__)

@app.route('/')
def result():
    #x = calcScore()
    return render_template('index.html', x = dict, y = KEYS, calcScore=calcScore)

if __name__ == '__main__':
   app.run(debug = True)