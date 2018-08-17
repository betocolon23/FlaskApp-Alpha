from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, validators, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(Form):
  name = StringField("Name",  [DataRequired("Please enter your name.")])
  email = StringField("Email",  [DataRequired("Please enter your email address."), Email("This field requires a valid email address")])
  subject = StringField("Subject",  [DataRequired("Please enter a subject.")])
  message = TextAreaField("Message",  [DataRequired("Please enter a message")])
  submit = SubmitField("Send")
