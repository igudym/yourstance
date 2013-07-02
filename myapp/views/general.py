from flask import Blueprint, render_template
from flask.ext.login import current_user

from myapp.forms.users import LoginForm

mod = Blueprint('general', __name__)
#mod = Blueprint('core', __name__, template_folder='templates', static_folder='static')

@mod.route('/')
def index():
	return render_template('general/index.html', user=current_user)
