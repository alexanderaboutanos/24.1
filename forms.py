"""Form for adding a pet!  """

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")


# class UserForm(FlaskForm):
#     """Form for adding/editing friend."""

#     name = StringField("Name",
#                        validators=[InputRequired()])
#     email = StringField("Email Address",
#                         validators=[Optional(), Email()])