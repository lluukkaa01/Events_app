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

@app.route('/events')
def event_page():
    id = request.args.get('id')
    if id:
        events = [events.to_dict() for events in Event.query.filter(Event.id == id)]
        return render_template('get_event.html', events=events)


@app.route('/filter', methods=['GET'])
def filter_events():
    event = request.args.get('event')
    print(event)
    events = [events.to_dict() for events in Event.query.filter(Event.event_name == event)]
    a = []
    print(events)
    if event == '':
        events = [events.to_dict() for events in Event.query.all()]
    elif events:
        pass
    elif events == a:
        events = [events.to_dict() for events in Event.query.filter(Event.description == event)]
    return render_template('index.html', events=events)


@app.route('/update', methods=['GET', 'PUT', 'POST'])
def update():
    id = request.args.get('id')
    event = Event.query.filter(Event.id==id).first()
    form = Events()
    if form.validate_on_submit():
        event_name = form.event_name.data
        description = form.description.data
        category = form.category.data
        holding_time = form.holding_time.data
        location = form.location.data
        age_restriction = form.age_restriction.data
        if event is not None:
            event.event_name = event_name
            event.description = description
            event.category = category
            event.event_name = event_name
            event.holding_time = holding_time
            event.location = location
            event.age_restriction = age_restriction
            db.session.commit()
        return redirect(url_for('updated'))
    return render_template('update.html', form=form, event=event)


@app.route('/updated')
def updated():
    massage = f"Successfully updated"
    return render_template('success page.html', massage=massage)




@app.route('/delete')
def delete_event():
    id = request.args.get('id')
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    massage = f"Event successfully deleted"
    return render_template('success page.html', massage=massage)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/')
def index():
    event = [events.to_dict() for events in Event.query.all()]
    return render_template('index.html', events=event)




with app.app_context():
    db.create_all()
