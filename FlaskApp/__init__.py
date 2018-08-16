from flask import Flask, render_template, redirect, url_for, request, flash
from forms import ContactForm
from flask_mail import Mail, Message


mail = Mail()

app = Flask(__name__)

app.secret_key = 'albertocolonnegron1995'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'betocolon23@gmail.com'
app.config["MAIL_PASSWORD"] = 'Tobe2013'
 
mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='betocolon23@gmail.com', recipients=['betocolon23@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
   app.run(debug=True)