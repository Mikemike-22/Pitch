from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required 

class PitchForm(FlaskForm):
    pitch = TextAreaField('Write Your Pitch',validators=[Required()])
    pitch_category = SelectField('Pitch Category',choices=[('Technology-Pitch','Technology Pitch'),('Business-Pitch','Business Pitch'),('Interview-Pitch','Interview Pitch'),('Pickup-Line','Pickup-Line Pitch'),('Promotion-Pitch','Promotion Pitch')],validators=[Required()])
    submit = SubmitField('Submit Pitch')
