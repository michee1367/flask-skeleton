#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class SolarPotential(db.Model):
    '''table des potentielle solaire.'''

    __tablename__ = 'solar_and_wind_potential_solar'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    siteName = db.Column(db.String(80), nullable=False) # nom
    solarRadiation = db.Column(db.Float, nullable=False)  # "Rayonnement solaire [KWh/m 2 /jour]"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<solar_and_wind_potential_solar %r>' % self.siteName