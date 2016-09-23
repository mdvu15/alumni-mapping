import os
from flask import Flask
from flask.json import JSONEncoder
from flask.ext.sqlalchemy import SQLAlchemy
from flask_jsglue import JSGlue
from config import basedir

app = Flask(__name__)
jsglue = JSGlue(app)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'alumni.db')
db = SQLAlchemy(app)

from alumni import views, models
