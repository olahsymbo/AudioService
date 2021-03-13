import os
import sys
import inspect


app_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(app_path))

sys.path.insert(0, module_dir)

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from db_config import *

connect = os.environ.get('connect')
app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Song(db.Model):
    __tablename__ = 'song'

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    name = db.Column('name', db.String(100), nullable=False)
    duration = db.Column('duration', db.Integer, nullable=False)
    uploaded_at = db.Column('uploaded_at', db.DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, name, duration, uploaded_at):
        self.name = name
        self.duration = duration
        self.uploaded_at = uploaded_at

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "duration": self.duration,
                "uploaded_at": self.uploaded_at}


class Podcast(db.Model):
    __tablename__ = 'podcast'

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    name = db.Column('name', db.String(100), nullable=False)
    duration = db.Column('duration', db.Integer, nullable=False)
    host = db.Column('host', db.String(100), nullable=False)
    participants = db.Column('participants', ARRAY(db.String(100)), nullable=True)
    uploaded_at = db.Column('uploaded_at', db.DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, name, duration, host, participants, uploaded_at):
        self.name = name
        self.duration = duration
        self.host = host
        self.participants = participants
        self.uploaded_at = uploaded_at

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "uploaded_at": self.uploaded_at}


class AudioBook(db.Model):
    __tablename__ = 'audiobook'

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    title = db.Column('title', db.String(100), nullable=False)
    author = db.Column('author', db.String(100), nullable=False)
    narrator = db.Column('narrator', db.String(100), nullable=False)
    duration = db.Column('duration', db.Integer, nullable=False)
    uploaded_at = db.Column('uploaded_at', db.DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, title, author, narrator, duration, uploaded_at):
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.uploaded_at = uploaded_at

    def serialize(self):
        return {"id": self.id,
                "title": self.title,
                "author": self.author,
                "uploaded_at": self.uploaded_at}

