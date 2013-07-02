from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

from myapp.forms.users import LoginForm
from myapp.forms.users import RegisterForm
from myapp.models.users import User

mod = Blueprint('users', __name__)

@mod.route('/')
def index():
    return render_template('users/index.html')

@mod.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(key=User.key(form.email.data),
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        user.put()
        flash("You are successfully registered.")
        return redirect(url_for("general.index"))
    return render_template('users/register.html', form=form)

@mod.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        # login and validate the user...
        user = User.get_by_id(form.email.data)
        if user and form.password.data == user.password:
            login_user(user)
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("general.index"))
        else:
            flash("Wrong user name or password")
    return render_template("users/login.html", form=form)

@mod.route("/account")
@login_required
def settings():
    return render_template('users/account.html')

@mod.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("general.index"))
