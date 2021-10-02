from flask import Flask, render_template
from markupsafe import escape
import os

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired



# instantiating an instance from Flask class
app = Flask(__name__)


# wtf token
WTForms_KEY = os.environ.get("WTForms_KEY")
app.config["SECRET_KEY"] = WTForms_KEY

# create a form class
class NameForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired("Name field should not be empty.")])

  submit = SubmitField("Submit")

# class NameForm(FlaskForm):
#   name     = StringField('Username', [validators.Length(min=4, max=25)])
  

# main webpage
@app.route("/")
def homepage():
  return render_template(escape("index.html"))

# users route
@app.route("/user/<name>")
def user(name): 
  first_name = "john"
  last_name = "smith"
  return render_template(
    escape("user.html"), 
    username=name,
    first_name=first_name,
    last_name=last_name
    )

# form
@app.route("/name", methods=["Get", "POST"])
def name():
  form = NameForm()
  name=None   
  
  # validate form
  if form.validate_on_submit():
    name = form.name.data 
    print(name)

    # reset form text field
    form.name.data = ""

  return render_template(
    escape("name.html"),
    name=name,
    form=form
  )

# pizza menu 
@app.route("/pizza")
def menu():
  menu_list = ["pepperoni", "mushroom", "margherita", "veggie"]
  print(menu_list)
  return render_template(
    escape("menu.html"),
    pizza=menu_list
  )

# Errors handling routes:

# Error 404 - Page not found
@app.errorhandler(404)
def page_not_found(err):
  return render_template(
    escape("error_404.html"), err=err), 404

# Server Error
@app.errorhandler(500)
def server_not_found(err):
  return render_template(escape("error_500.html"), err=err), 500


# form route
# @app.route("/name", methods=["Get", "POST"])
# def name():
#   form = NameForm()

#   name=None
#   if form.validate_on_submit():
#     name = form.name.data
#     # reset form text field
#     form.name.data = ""

#   return render_template(
#     escape("name.html"),
#     name=name,
#     form=form
#   )
