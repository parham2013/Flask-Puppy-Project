import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:7421@localhost:5432/normal-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')