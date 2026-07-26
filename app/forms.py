from flask_babel import lazy_gettext as _l
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    email = EmailField(_l("Email Address"), validators=[DataRequired(), Email()])
    password = PasswordField(_l("Password"), validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(_l("Login"))


class RegisterForm(FlaskForm):
    name = StringField(
        _l("Name"),
        validators=[
            DataRequired(message=_l("Please enter your name.")),
            Length(max=126, message=_l("Name must be 126 characters or fewer.")),
        ],
        description=_l("Enter your full name."),
    )
    email = EmailField(
        _l("Email Address"),
        validators=[
            DataRequired(message=_l("Please enter your email address.")),
            Email(message=_l("Please enter a valid email address.")),
        ],
        description=_l("Enter the email address for your account."),
    )
    password = PasswordField(
        _l("Password"),
        validators=[
            DataRequired(message=_l("Please enter a password.")),
            Length(min=8, message=_l("Password must be at least 8 characters long.")),
        ],
        description=_l("Choose a secure password with at least 8 characters."),
    )
    submit = SubmitField(_l("Create Account"))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                _l("Email already registered. Please choose a different email.")
            )


class ProfileEditForm(FlaskForm):
    name = StringField(
        _l("Name"),
        validators=[
            Length(max=126, message=_l("Name must be 126 characters or fewer.")),
        ],
        description=_l("Enter your full name."),
    )
    email = EmailField(
        _l("Email Address"),
        validators=[
            Email(message=_l("Please enter a valid email address.")),
        ],
        description=_l("Enter your email address."),
    )
    submit = SubmitField(_l("Update"))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user and user.id != current_user.id:
            raise ValidationError(
                _l("Email already registered. Please choose a different email.")
            )
