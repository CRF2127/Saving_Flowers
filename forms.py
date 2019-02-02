from flask_wtf import Form
from wtforms import StringField, SubmitField

class postform(Form):
	title = StringField('Title')
	subtitle = StringField('Subtitle')
	author = StringField('Author')
	content = StringField('Content')