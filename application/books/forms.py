from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BookForm(FlaskForm):
    name = StringField("Book title", [validators.Length(min=2)])
    author = StringField("Book author", [validators.Length(min=2)])
    publication_year = IntegerField("Publication year")

    class Meta:
        csrf = False
class UpdateForm(FlaskForm):
    name = StringField("Book title", [validators.Length(min=2)])
    author = StringField("Book author", [validators.Length(min=2)])
    publication_year = IntegerField("Publication year")

    class Meta:
        csrf = False
