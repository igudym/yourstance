from flask import Blueprint, render_template

from libs.flask_login import login_user, logout_user, current_user, login_required

from myapp.forms.users import LoginForm
from myapp.forms.users import RegisterForm

mod = Blueprint('users', __name__)

@mod.route('/')
def index():
	return render_template('users/index.html')

@mod.route('/register')
def index():
	return render_template('users/register.html')

@mod.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# login and validate the user...
		login_user(user)
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template("users/login.html", form=form)

@mod.route("/account")
@login_required
def settings():
	return render_template('users/account.html')

@mod.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(somewhere)
