import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'hjgjghjghjghjghjgjhghjghjghj76'
ADMINS = frozenset(['http://lucumr.pocoo.org/'])

THREADS_PER_PAGE = 15

del os
