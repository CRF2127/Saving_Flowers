from flask import Flask, render_template
#from models import db, posts
from forms import postform
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/saving_flowers'
db = SQLAlchemy(app)
#db.init_app(app)

class BlogPost(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	content = db.Column(db.Text)
	entry_date = db.Column(db.DateTime)

@app.route("/")
def index():
	posts=BlogPost.query.all()
	return render_template("index.html" , post=posts)

@app.route("/about")
def about():
	return render_template("about.html")

#@app.route('/testForm')
#def test():
	#form = postform

if __name__ == "__main__":
	app.run(debug=True)