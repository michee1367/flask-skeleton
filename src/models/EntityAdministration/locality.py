#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class Locality(db.Model):
    '''table des localité.'''

    __tablename__ = 'locality'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    population = db.Column(db.Integer, nullable=False) # population
    area = db.Column(db.Float, nullable=False) # surface
    income = db.Column(db.Float, nullable=False) # Revenu total
    name = db.Column(db.String(80), nullable=False) # nom

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<province %r>' % self.name