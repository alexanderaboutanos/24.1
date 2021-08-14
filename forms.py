"""Form for adding a pet!  """

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

species_choices = ["cat", "dog", "porcupine"]

class PetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name")
    species = SelectField("Species", choices=[(s,s) for s in species_choices])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(0,30)])
    notes = StringField("Notes")

