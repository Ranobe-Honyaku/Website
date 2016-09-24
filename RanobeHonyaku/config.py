import os
from utils import setup_file

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = setup_file["SECRET_KEY"]

# This database should be for development only
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')