from flask_sqlalchemy import SQLAlchemy
#flask.ext.sqlalchemy

db = SQLAlchemy()

class posts(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	content = db.Column(db.Text)
	entry_date = db.Column(db.DateTime)
	
	def __init__(self, id, title, subtitle, author, date_posted, content):
		self.title = title.title()
		self.subtitle = subtitle.title()
		self.author = author.title()
		self.date_posted = date_posted.date()
		self.content = content.string()