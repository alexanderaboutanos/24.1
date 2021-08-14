from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///agency"


debug = DebugToolbarExtension(app)

# connect_db(app)


@app.route('/')
def show_pet_list():
    return render_template('pet_list.html')

