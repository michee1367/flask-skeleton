#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class EconomicActivity(db.Model):
    '''table des Activité économique.'''

    __tablename__ = 'local_economy_economic_activity'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currentProduction = db.Column(db.Float, nullable=False)  # "Production actuelle [quantité en kg,tonne…]"
    potentialProduction = db.Column(db.Float, nullable=False)  # "Production potentielle [quantité en kg,tonne…]"
    estimatedConsumption = db.Column(db.Float, nullable=False)  # "Consommation estimée lorsqu’existante"
    
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<local_economy_economic_activity %r>' % self.estimatedConsumption