from flask import Flask, render_template
from markupsafe import escape


# instantiating an instance from Flask class
app = Flask(__name__)


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


