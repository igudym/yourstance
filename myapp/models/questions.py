from google.appengine.ext import ndb

class Question(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	modified = ndb.DateTimeProperty(auto_now=True)
	question = ndb.StringProperty(required=True)
	slug = ndb.StringProperty(required=True)
	num_votes = ndb.IntegerProperty(default=0)
	num_reasons = ndb.IntegerProperty(default=0)
	num_posts = ndb.IntegerProperty(default=0)

	def put (self):
		if Question.gql ('WHERE slug = :1', self.slug).count() > 0:
			raise UniqueConstraintViolation ("slug", self.slug)
		ndb.Model.put (self)

class UniqueConstraintViolation(Exception):
	def __init__(self, scope, value):
		super(UniqueConstraintViolation, self).__init__("Value '%s' is not unique within scope '%s'." % (value, scope, ))