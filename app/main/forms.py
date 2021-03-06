from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from ..models import User



class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[DataRequired()])
    review = TextAreaField('Movie review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

# class ReviewForm(FlaskForm):

#      title = StringField('Review title',validators=[DataRequired()])

#      review = TextAreaField('Movie review')

#      submit = SubmitField('Submit')

