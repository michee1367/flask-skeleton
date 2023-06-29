#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class ExistingPlants(db.Model):
    '''table des secteurs.'''

    __tablename__ = 'existing_plant_existing_plant'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom
    power = db.Column(db.Float, nullable=False)  # "Puissance installée/ disponible [KW]"
    nbrOfhouseholds = db.Column(db.Integer, nullable=False) # "Nombre de ménages connectés"
    powerForProductiveUsed = db.Column(db.Float, nullable=False) # "Puissance ménages [KW]"
    powerForProductiveUsed = db.Column(db.Float, nullable=False) # "Puissance usage productif/ industriel"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_plant_existing_plant %r>' % self.name