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




with app.app_context():
    db.create_all()