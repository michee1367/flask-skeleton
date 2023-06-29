#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class HealthZone(db.Model):
    '''table des zones de santé.'''

    __tablename__ = 'health_health_zone'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # "Nom Zone de santé"
    population = db.Column(db.Integer, nullable=False)  # "population de la Zone de santé"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<health_health_zone %r>' % self.name