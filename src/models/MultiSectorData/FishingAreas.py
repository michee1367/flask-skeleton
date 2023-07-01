#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class FishingAreas(db.Model):
    '''table des Zones de pêche.'''

    __tablename__ = 'multi_sector_data_fishing_areas'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # "Nom Etablissement de santé"
    estimatedConsumption = db.Column(db.Float, nullable=False)  # "Consommation estimée lorsqu’existante"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<multi_sector_data_fishing_areas %r>' % self.wording