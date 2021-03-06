from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField,SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=4, max=15)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=4, max=15)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=80)])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class PostForm(FlaskForm):
    author = StringField('Author Name', validators=[InputRequired(), Length(min=4, max=15)])
    description = StringField('First Name', validators=[InputRequired(), Length(min=4, max=200)])
    submit = SubmitField('Submit Blog')

class CommentForm(FlaskForm):
body = StringField('', validators=[DataRequired()])
submit = SubmitField('Submit')