#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class WindPotential(db.Model):
    '''table des potentielle heleolien.'''

    __tablename__ = 'solar_and_wind_potential_wind'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    siteName = db.Column(db.String(80), nullable=False) # nom
    windSpeed = db.Column(db.Float, nullable=False)  # "Rayonnement vent [m/s]"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<solar_and_wind_potential_wind %r>' % self.siteName