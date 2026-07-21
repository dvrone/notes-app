from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Please enter your name."),
            Length(max=126, message="Name must be 126 characters or fewer."),
        ],
        description="Enter your full name.",
    )
    email = EmailField(
        "Email Address",
        validators=[
            DataRequired(message="Please enter your email address."),
            Email(message="Please enter a valid email address."),
        ],
        description="Enter the email address for your account.",
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Please enter a password."),
            Length(min=8, message="Password must be at least 8 characters long."),
        ],
        description="Choose a secure password with at least 8 characters.",
    )
    submit = SubmitField("Create Account")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "Email already registered. Please choose a different email."
            )
