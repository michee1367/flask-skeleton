#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class DistributionNetwork(db.Model):
    '''table des reseaux de distribution.'''

    __tablename__ = 'drinking_water_supply_distribution_network'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<drinking_water_supply_distribution_network %r>' % self.wording