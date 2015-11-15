from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length

class HideForm(Form):
    '''WTForm Hide Image form'''
    message = TextAreaField(u'Enter Your Message Here', validators=[DataRequired(), Length(max=140), message="You must enter a message that is less than 140 characters long"])
    password = StringField(u'Password for encryption', validators=[DataRequired])

class RevealForm(Form):
    password = StringField(u'Password for decryption', validators=[DataRequired])
