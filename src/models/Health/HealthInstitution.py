#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class HealthInstitution(db.Model):
    '''table des institution de santé.'''

    __tablename__ = 'health_health_institution'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # "Nom Etablissement de santé"
    accommodationCapacity = db.Column(db.Float, nullable=False)  # "Capacité d’accueil de l’établissement [nombre de personnes]"
    estimatedConsumption = db.Column(db.Integer, nullable=False)  # "Consommation estimée lorsqu’existante"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<health_health_institution %r>' % self.name