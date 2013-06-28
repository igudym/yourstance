from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField, RadioField
from flask.ext.wtf import Required, Length, validators
#from flask.ext.uploads import UploadSet, IMAGES

from google.appengine.ext import ndb
from myapp.models.questions import Question

def unique_slug(form, field):
    if Question.gql ('WHERE slug = :1', field.data).count() > 0:
        raise validators.ValidationError('That slug is already in use, please select another.')

class QuestionForm(Form):
    question = TextField('Question', [validators.Length(min=4, max=225)])
    slug = TextField('Slug', validators = [validators.Required(), validators.length(max=200),  
unique_slug])

   