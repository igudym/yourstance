from flask import Blueprint, render_template, redirect, url_for, request

from myapp.forms.questions import QuestionForm
from myapp.models.questions import Question

mod = Blueprint('questions', __name__, url_prefix='/q')

@mod.route('/')
def index():
	questions = Question.query()
	return render_template('questions/index.html', questions=questions)

@mod.route('/new', methods = ['GET', 'POST'])
def new():
	form = QuestionForm(request.form, csrf_enabled=False)
	if request.method=='POST':
		if form.validate_on_submit():
			q = Question()
			q.question = form.data.get('question')
			q.slug = form.data.get('slug')
			q.put()
			#flash(u'%s was saved.' % item.name, 'success')
			return redirect(url_for('questions.index'))
	return render_template('questions/new.html', form=form)

