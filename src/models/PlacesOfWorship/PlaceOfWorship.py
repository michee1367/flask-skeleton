#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class PlaceOfWorship(db.Model):
    '''table des lieux de culte.'''

    __tablename__ = 'place_of_worship_place_of_worship'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # "Nom Etablissement de santé"
    accommodationCapacity = db.Column(db.Float, nullable=False)  # "Capacité d’accueil de l’établissement [nombre de personnes]"
    estimatedConsumption = db.Column(db.Integer, nullable=False)  # "Consommation estimée lorsqu’existante"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<place_of_worship_place_of_worship %r>' % self.name