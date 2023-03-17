"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name",
                       validators=[InputRequired()])

    species = StringField("Species",
                          validators=[InputRequired(),
                                      AnyOf(values=["cat",
                                                    "dog",
                                                    "porcupine"])])

    photo_url = StringField("Photo URL",
                            validators=[Optional(),
                                        URL(require_tld=False)])

    age = SelectField('Age',
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')],
                      validators=[AnyOf(values=["baby",
                                                "young",
                                                "adult",
                                                "senior"]),
                                  InputRequired()])

    notes = TextAreaField("Notes",
                          validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField("Photo URL",
                            validators=[Optional(),
                                        URL(require_tld=False)])

    notes = TextAreaField("Notes",
                          validators=[Optional()])

    available = BooleanField('Available?')
