from flask import Flask 
from flask import url_for, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('news.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

if __name__ == '__main__':
    app.run(debug=True, port=5502)