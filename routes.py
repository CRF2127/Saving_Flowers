from flask import Flask, render_template
from forms import postform
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qkcsiwgxujewdk:af5c7e62105555843601c77b5c450b8761357ddbc5cc89f8048201a52ab4074c@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d8ot5pbfnhl1nc'
#'postgresql://localhost/saving_flowers'

db = SQLAlchemy(app)

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
	posts=BlogPost.query.order_by(BlogPost.entry_date.desc()).all()
	return render_template("index.html" , posts=posts)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/post/<int:post_id>")
def post(post_id):
	posts=BlogPost.query.filter_by(id=post_id).one()

	return render_template("post.html", posts=posts)

if __name__ == "__main__":
	app.run(debug=True)