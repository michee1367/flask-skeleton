#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class IndividualSet(db.Model):
    '''table des Kit individuel.'''

    __tablename__ = 'individual_sets_individual_set'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    powerAvailable = db.Column(db.Float, nullable=False) # "Puissance disponible [KW]"
    nbrhouseholdsConnected = db.Column(db.Integer, nullable=False) # "Nombre de ménages connectés"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_powerLines_power_line %r>' % self.name