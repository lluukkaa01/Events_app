from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class Events(FlaskForm):
    event_name = StringField('Event name', validators=[validators.DataRequired()])
    description = StringField('Description', validators=[validators.DataRequired()])
    category = StringField('Event category', validators=[validators.DataRequired()])
    holding_time = StringField('Holding time', validators=[validators.DataRequired()])
    location = StringField('Location', validators=[validators.DataRequired()])
    age_restriction = StringField('Age restriction', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')