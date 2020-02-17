from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import Form
from wtforms.fields.html5 import DateField

class LocationForm(FlaskForm):
    ip = StringField("IP Address: ")
    submit = SubmitField ("Get Location")
    history = SubmitField("Get search history")

class DatesForm(Form):
    start_date = DateField('Start Date', format='%m/%d/%Y')
    end_date = DateField('End Date', format='%m/%d/%Y')
    submit = SubmitField ("Submit Dates")
    last_n = StringField("Last N Locations")