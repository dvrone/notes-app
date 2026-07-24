from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.forms import LoginForm, RegisterForm
from app.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Welcome back!", "info")
            next_page = request.args.get("next", None)
            return redirect(next_page or url_for("main.index"))
        else:
            flash("Email or password incorrect!", "danger")
    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            name=form.name.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Your account created successfully", "success")
        return redirect(url_for("main.index"))
    return render_template("auth/register.html", form=form)
