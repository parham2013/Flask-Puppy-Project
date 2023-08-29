from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    name = StringField('Name of Owner:')
    puppy_id = IntegerField('Id of Puppy:')
    submit = SubmitField('Add Owner')