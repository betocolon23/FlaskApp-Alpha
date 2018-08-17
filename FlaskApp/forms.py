from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, validators, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(Form):
  name = StringField("Nombre",  [DataRequired("Entre su nombre.")])
  email = StringField("Email",  [DataRequired("Entre un correo electronico"), Email("Este campo conlleva un email valido")])
  subject = StringField("Sujeto",  [DataRequired("Entre un sujeto")])
  message = TextAreaField("Mensaje",  [DataRequired("Entre un Mensaje")])
  submit = SubmitField("Enviar")
