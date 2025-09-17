from flask import Flask 
from flask import url_for, render_template
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config(SQLAlCHEMY_DATABASE_URI = 'sqlite:///our_database.db')
# db = SQLAlchemy(app)
# class Post(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  title = db.Column(db.String(300), nullable=False)
#  text = db.Column(db.Text, nullable=False)
# with app.app_context():
#      db.create_all()
#      print("database is done")

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