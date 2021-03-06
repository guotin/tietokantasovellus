from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=10)])
    password = PasswordField("Password", [validators.Length(min=4, max=20)])

    class Meta:
        csrf = False
        
class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=10), validators.DataRequired()])
    password = PasswordField("Password", [validators.Length(min=4, max=20), validators.DataRequired()])

    class Meta:
        csrf = False
