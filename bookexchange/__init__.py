# bookexchange/__init__.py

# Import Section
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

################################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
################################################################
######## DATABASE SETUP ########################################
################################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

###############################################################