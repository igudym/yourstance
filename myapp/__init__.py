import os
import sys
import logging

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'libs'))

from flask import Flask, session, g, render_template

from libs.flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('websiteconfig')

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.setup_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(exception):
	return "Some internal error has taken place.  Alert somebody!"

from myapp.views import general
from myapp.views import users
from myapp.views import questions
app.register_blueprint(general.mod)
app.register_blueprint(users.mod)
app.register_blueprint(questions.mod)