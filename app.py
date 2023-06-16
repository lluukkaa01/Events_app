from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from events import Events

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Events.db'

db = SQLAlchemy(app)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(20))
    description = db.Column(db.String(200))
    category = db.Column(db.String(20))
    holding_time = db.Column(db.String(20))
    location = db.Column(db.String(50))
    age_restriction = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'event_name': self.event_name,
            'description': self.description,
            'category': self.category,
            'holding_time': self.holding_time,
            'location': self.location,
            'age_restriction': self.age_restriction,

        }
