from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, validators

class ReviewForm(FlaskForm):
    grade = IntegerField("Review grade", [validators.NumberRange(min=0, max=5)])
    text = TextAreaField("Review text", [validators.Length(min=10,max=300), validators.DataRequired()])

    class Meta:
        csrf = False

