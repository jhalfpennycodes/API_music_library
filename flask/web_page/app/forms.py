from flask import Flask
from flask_wtf import FlaskForm as Form
from wtforms import SelectField, validators, StringField
from wtforms.validators import DataRequired


class EraForm(Form):
    era = SelectField("Genre", choices=['60s', '70s', '80s', '90s', '2000s'])

