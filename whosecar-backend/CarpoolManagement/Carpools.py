from whosecar import db


class Carpool(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    Title = db.Column(db.String(64))
    DateCreated = db.Column(db.TIMESTAMP)

    Cars = db.relationship('Cars', backref='carpool', lazy=True)


class Cars(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    OwnerName = db.Column(db.String(24))
    CarCapacity = db.Column(db.Integer)
    TimeCreated = db.Column(db.TIMESTAMP)
    carpool_id = db.Column(db.String(8), db.ForeignKey('carpool.id'))

    Passengers = db.relationship('CarPassengers', backref='cars', lazy=True)


class CarPassengers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.String(8), db.ForeignKey('cars.id'))
    TimeSelected = db.Column(db.TIMESTAMP)
    PassengerName = db.Column(db.String(24))