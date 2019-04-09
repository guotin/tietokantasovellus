from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BookForm(FlaskForm):
    name = StringField("Book title", [validators.Length(min=2, max=30), validators.DataRequired()])
    author = StringField("Book author", [validators.Length(min=2, max=30), validators.DataRequired()])
    publication_year = IntegerField("Publication year", [validators.NumberRange(min=-3000, max=3000)])

    class Meta:
        csrf = False

