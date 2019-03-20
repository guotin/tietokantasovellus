from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, validators

class ReviewForm(FlaskForm):
    grade = IntegerField("Review grade", [validators.NumberRange(min=0, max=5)])
    text = TextAreaField("Review text", [validators.Length(max=300)])

    class Meta:
        csrf = False

