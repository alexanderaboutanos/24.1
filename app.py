from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_pet_list():
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add')
def show_add_pet_form():
    
    form = AddPetForm()
    
    return render_template('add_pet_form.html', form=form)

