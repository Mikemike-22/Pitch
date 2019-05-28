from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required 

class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment here',validators=[Required()])
    submit = SubmitField('Submit Comment')
